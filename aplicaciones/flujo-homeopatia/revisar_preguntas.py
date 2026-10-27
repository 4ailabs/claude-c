#!/usr/bin/env python3
"""TRÍPODE · Revisor de preguntas: ninguna pregunta al paciente debe inducir un remedio (regla de oro 6).

Rechaza una pregunta si:
  - nombra un remedio o su abreviatura (lista de la tabla `remedios` del repertorio local);
  - se contesta con sí o no (no empieza con cómo / qué / cuándo / dónde / cuál / cuánto / por qué, ni ofrece dos polos);
  - ofrece un menú "por ejemplo…" o termina en "¿no?" / "¿verdad?" (sugiere la respuesta);
  - pregunta por un solo polo de una modalidad ("¿empeora con el frío?").
El revisor no redacta por el modelo: dice qué falla y cómo se ve la forma abierta.

    python3 revisar_preguntas.py preguntas.txt          # una pregunta por línea (o JSON con una lista de textos)
    echo "¿Le arden los pies?" | python3 revisar_preguntas.py -

Sale con 0 si todas pasan y 1 si alguna se rechaza.
"""
import argparse
import json
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

DB = Path(__file__).resolve().parents[3] / "referencias" / "repertorio" / "repertorio.db"
ABIERTAS = re.compile(r"^(como|que|cual|cuales|cuando|desde cuando|hasta cuando|donde|cuanto|cuanta|cuantos|cuantas|por que|para que|quien|en que|de que|"
                      r"a que|con que|cuenteme|platiqueme|digame|describa|describame|hableme|que pasa)\b"
                      # "¿Hay algo / alguna hora en que…?" es abierta; "¿Hay alguna reacción de ardor?" nombra el síntoma: cerrada.
                      r"|^hay (algo|alguna|algun|algunas|algunos)\b.*\bque\b")
POLOS = re.compile(r"\b(peor|mejor|empeora|mejora|agrava|alivia|calma)\b")
# Palabras del español que coinciden con nombres de remedios y no deben contarse como tales.
ESPANOL = {"china", "ruta", "acido", "acidum", "plata", "oro", "arena", "sal", "salvia", "menta",
           "caliente", "petroleo", "nitri", "trigo", "avena", "cafe", "cacao", "tabaco", "hierro", "cobre", "zinc"}
RESPALDO = {"sulphur", "sulph", "pulsatilla", "puls", "natrum", "nat-m", "lycopodium", "calcarea", "calc", "phosphorus", "phos",
            "sepia", "arsenicum", "nux-v", "nux", "lachesis", "lach", "staphysagria", "staph", "ignatia", "hepar", "phytolacca",
            "medorrhinum", "carcinosin", "gelsemium", "bryonia", "rhus", "belladonna", "silicea", "thuja", "causticum", "aurum"}


def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s-]", " ", s)).strip()


def lexico_remedios(db):
    if not db.exists():
        return RESPALDO
    con = sqlite3.connect(db)
    lex = set()
    for abrev, nombre in con.execute("SELECT abrev, nombre FROM remedios"):
        if abrev and (len(abrev) >= 4 or "-" in abrev):
            lex.add(abrev.lower())
        primera = norm(nombre or "").split(" ")[0]
        if len(primera) >= 5:
            lex.add(primera)
    return (lex | RESPALDO) - ESPANOL


def revisar(pregunta, lex):
    # "Me dijo que X. ¿Desde cuándo…?": se juzga la pregunta, no el recordatorio con las palabras del paciente.
    p = norm(pregunta[pregunta.index("¿"):] if "¿" in pregunta else pregunta)
    motivos = []
    palabras = set(p.split())
    remedios = sorted(w for w in palabras if w in lex)
    if remedios:
        motivos.append(f"nombra un remedio ({', '.join(remedios)}): la pregunta se redacta sin conocer candidatos")
    dos_polos = bool(re.search(r" o (?!sea\b)", f" {p} "))  # "o sea" es muletilla, no una alternativa
    if "por ejemplo" in p:
        motivos.append("ofrece un menú «por ejemplo…»: sugiere la respuesta")
    if re.search(r"(\bno|verdad)\s*$", p) and "?" in pregunta:
        motivos.append("termina en «¿no?»/«¿verdad?»: sugiere la respuesta")
    abierta = bool(ABIERTAS.match(p))
    if not abierta and not dos_polos:
        motivos.append("se contesta con sí o no: empiece con cómo / qué / cuándo / dónde, o ofrezca los dos polos")
    if not abierta and POLOS.search(p) and not dos_polos and not ("peor" in palabras and "mejor" in palabras):
        motivos.append("pregunta por un solo polo: pregunte por el eje (¿cómo le va con…?, ¿qué lo mejora y qué lo empeora?)")
    return motivos


def leer(origen):
    texto = sys.stdin.read() if origen == "-" else Path(origen).read_text(encoding="utf-8")
    try:
        data = json.loads(texto)
        if isinstance(data, list):
            return [str(x) for x in data]
    except json.JSONDecodeError:
        pass
    return [l.strip(" -•\t") for l in texto.splitlines() if l.strip()]


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("preguntas")
    ap.add_argument("--db", type=Path, default=DB, help=argparse.SUPPRESS)
    a = ap.parse_args()
    lex = lexico_remedios(a.db)
    rechazadas = 0
    for q in leer(a.preguntas):
        motivos = revisar(q, lex)
        rechazadas += bool(motivos)
        print(("RECHAZADA  " if motivos else "OK         ") + q)
        for m in motivos:
            print(f"           ↳ {m}")
    print(f"\n{rechazadas} rechazada(s).")
    sys.exit(1 if rechazadas else 0)
