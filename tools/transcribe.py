# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx>=0.27"]
# ///
"""Transcribe una grabación con Voxtral (Mistral) y escribe Markdown.

Divide el audio en trozos con ffmpeg (las sesiones duran horas), transcribe cada
trozo y los une con marcas de tiempo.

    uv run tools/transcribe.py recordings/01.m4a --out transcripts/01-.../sesion.md
    uv run tools/transcribe.py recordings/01.m4a --dry-run   # solo corta, no llama a la API
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import httpx

API_URL = "https://api.mistral.ai/v1/audio/transcriptions"
RETRY_STATUS = {429, 500, 502, 503, 504}


def load_dotenv(path: Path) -> None:
    if not path.is_file():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def duration_seconds(audio: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(audio)],
        check=True, capture_output=True, text=True,
    ).stdout
    return float(out.strip())


def split_audio(audio: Path, chunk_s: int, workdir: Path) -> list[tuple[float, Path]]:
    """Corta en mp3 mono 16 kHz; devuelve [(inicio_en_segundos, archivo)]."""
    total = duration_seconds(audio)
    chunks: list[tuple[float, Path]] = []
    start = 0.0
    while start < total:
        out = workdir / f"chunk_{len(chunks):04d}.mp3"
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-ss", str(start), "-t", str(chunk_s),
             "-i", str(audio), "-vn", "-ac", "1", "-ar", "16000", "-b:a", "64k", str(out)],
            check=True,
        )
        chunks.append((start, out))
        start += chunk_s
    return chunks


def transcribe_chunk(client: httpx.Client, path: Path, args: argparse.Namespace) -> dict:
    # La API no admite `language` junto con timestamps por segmento: se elige uno.
    data: dict[str, str] = {"model": args.model}
    if args.timestamps:
        data["timestamp_granularities"] = "segment"
    else:
        data["language"] = args.language
    for attempt in range(1, args.retries + 1):
        with path.open("rb") as fh:
            resp = client.post(API_URL, data=data, files={"file": (path.name, fh, "audio/mpeg")})
        if resp.status_code not in RETRY_STATUS:
            resp.raise_for_status()
            return resp.json()
        wait = 2 ** attempt
        print(f"  {resp.status_code}, reintento {attempt}/{args.retries} en {wait}s", file=sys.stderr)
        time.sleep(wait)
    resp.raise_for_status()
    return resp.json()


def stamp(seconds: float) -> str:
    s = int(seconds)
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def render(parts: list[tuple[float, dict]], title: str) -> str:
    lines = [f"# {title}", ""]
    for offset, result in parts:
        segments = result.get("segments") or []
        if segments:
            for seg in segments:
                lines += [f"**[{stamp(offset + float(seg.get('start', 0)))}]** {seg['text'].strip()}", ""]
        else:
            lines += [f"**[{stamp(offset)}]** {result.get('text', '').strip()}", ""]
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("audio", type=Path)
    p.add_argument("--out", type=Path, help="Markdown de salida (por defecto transcripts/<nombre>.md)")
    p.add_argument("--model", default="voxtral-mini-latest")
    p.add_argument("--language", default="es")
    p.add_argument("--timestamps", action="store_true",
                   help="marcas por segmento (la API ignora --language en este modo)")
    p.add_argument("--chunk-minutes", type=int, default=10)
    p.add_argument("--retries", type=int, default=4)
    p.add_argument("--dry-run", action="store_true", help="solo corta el audio y lista los trozos")
    args = p.parse_args()

    if not args.audio.is_file():
        p.error(f"no existe {args.audio}")
    if not (shutil.which("ffmpeg") and shutil.which("ffprobe")):
        p.error("falta ffmpeg/ffprobe en el PATH")

    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
    key = os.environ.get("MISTRAL_API_KEY")
    if not key and not args.dry_run:
        p.error("define MISTRAL_API_KEY (en .env o en el entorno)")

    out_md = args.out or Path("transcripts") / f"{args.audio.stem}.md"
    out_md.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        chunks = split_audio(args.audio, args.chunk_minutes * 60, Path(tmp))
        print(f"{args.audio}: {len(chunks)} trozos de {args.chunk_minutes} min")
        if args.dry_run:
            for start, path in chunks:
                print(f"  {stamp(start)}  {path.name}  {path.stat().st_size / 1e6:.1f} MB")
            return 0

        parts: list[tuple[float, dict]] = []
        with httpx.Client(headers={"Authorization": f"Bearer {key}"}, timeout=300) as client:
            for i, (start, path) in enumerate(chunks, 1):
                print(f"[{i}/{len(chunks)}] {stamp(start)}")
                parts.append((start, transcribe_chunk(client, path, args)))

    out_md.write_text(render(parts, args.audio.stem), encoding="utf-8")
    out_md.with_suffix(".json").write_text(
        json.dumps([{"offset": o, **r} for o, r in parts], ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Listo: {out_md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
