"""Valida un caso depurado contra su transcripción (fases F1 y F3 del flujo de homeopatía).

Comprueba, sin usar ningún modelo:
  1. Que cada cita del caso exista tal cual en la transcripción. Un síntoma
     "repertorizable" sin cita encontrada baja a "informativo".
  2. La Regla de los Tres: al menos un síntoma repertorizable de nivel 1-2,
     uno de nivel 3 (SRP) y uno de nivel 4.
  3. (Opcional) Qué datos de un análisis previo aparecen o no en la grabación.

Uso:
    python3 validar_caso.py caso.json transcripcion.json [afirmaciones.json]

Sale con código 0 si se pueden nombrar candidatos y 1 si hay que pedir más datos.
"""
import json
import re
import sys
import unicodedata


def norm(s):
    s = unicodedata.normalize("NFC", s.lower())
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", s)).strip()


def texto_transcripcion(path):
    """Acepta el JSON de Voxtral ({segments: [...]}) o el de tools/transcribe.py ([{offset, segments}])."""
    data = json.load(open(path, encoding="utf-8"))
    partes = data if isinstance(data, list) else [data]
    textos = []
    for parte in partes:
        segmentos = parte.get("segments") or [{"text": parte.get("text", "")}]
        textos += [s.get("text", "") for s in segmentos]
    return norm(" ".join(textos))


def validar(caso, texto):
    print(f"Caso: {caso.get('paciente', '?')} · {caso.get('consulta', '?')}\n")
    niveles, bajados = set(), []
    for s in caso["sintomas"]:
        ok = norm(s["cita"]) in texto
        if s["clase"] == "repertorizable" and not ok:
            s["clase"] = "informativo"
            bajados.append(s["sintoma"])
        if s["clase"] == "repertorizable":
            niveles.add(s["nivel"])
        marca = "cita OK " if ok else "SIN CITA"
        print(f"  [{marca}] {s.get('t', '--:--')}  {s['clase']:<14} N{s.get('nivel') or '-'}  {s['sintoma']}")

    tres = {
        "Nivel 1-2 (mentales o generales)": bool(niveles & {1, 2}),
        "Nivel 3 (raro, peculiar)": 3 in niveles,
        "Nivel 4 (particular con modalidad)": 4 in niveles,
    }
    print("\nRegla de los Tres:")
    for k, v in tres.items():
        print(f"  {'✔' if v else '✘'} {k}")
    if bajados:
        print("\nBajados a informativo porque su cita no está en la transcripción:")
        for b in bajados:
            print(f"  - {b}")
    listo = all(tres.values())
    print("\n→", "Se pueden nombrar candidatos." if listo else "🔴 Pedir más datos antes de nombrar un remedio.")
    return listo


def revisar_afirmaciones(afirmaciones, texto):
    print("\nDatos del análisis previo frente a la grabación:")
    for a in afirmaciones:
        hit = re.search(a["patron"], texto)
        detalle = f"  («…{hit.group(0)}…»)" if hit else ""
        print(f"  [{'aparece' if hit else 'NO está'}] {a['dato']}{detalle}")


if __name__ == "__main__":
    if len(sys.argv) not in (3, 4):
        sys.exit(__doc__)
    caso = json.load(open(sys.argv[1], encoding="utf-8"))
    texto = texto_transcripcion(sys.argv[2])
    listo = validar(caso, texto)
    if len(sys.argv) == 4:
        revisar_afirmaciones(json.load(open(sys.argv[3], encoding="utf-8")), texto)
    sys.exit(0 if listo else 1)
