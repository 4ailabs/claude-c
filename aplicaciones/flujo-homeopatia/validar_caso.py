#!/usr/bin/env python3
"""TRÍPODE · F1v. Valida un caso depurado contra sus transcripciones, sin usar ningún modelo (v0.2).

Comprueba:
  1. Que cada cita exista tal cual y la haya dicho la PACIENTE (P4). Si solo la dice el doctor, es una pregunta, no un síntoma.
  2. El ORIGEN de cada dato (P17): una palabra clave que el doctor dijo primero (y la paciente no había dicho antes), un
     "sí/no" a una pregunta cerrada, un menú "por ejemplo…" de una sola opción o un "sí" conseguido al repreguntar con la
     misma palabra que ella había negado bajan el dato a `cerrada`. Nunca sube un origen declarado.
  3. La Regla de los Tres SOLO con datos firmes (espontaneo, abierta, dos_polos, observado). Un mental (nivel 1) cuenta
     solo si trae `contexto` (cuándo, con quién, desde qué).
  4. Por candidato (P2, P19), si el caso trae "candidatos": qué parte de su apoyo es firme, inducida o sin cita, si cumple
     la Regla de los Tres por sí solo y el semáforo máximo que permite.
  5. La calidad de la transcripción (P18): huecos de más de 60 s y hablantes.
  6. (Opcional) Qué datos de un análisis previo aparecen o no en la grabación (afirmaciones.json).

Escribe caso_validado.json junto a caso.json (o en --salida): cada síntoma con el `origen` que decidió el validador,
`origen_declarado`, `estado_cita`, `firme` (true/false) y `motivo_validador`. caso.json no se modifica.

Uso:
    python3 validar_caso.py caso.json transcripcion.json [otra_transcripcion.json …] [afirmaciones.json] [--paciente speaker_2]

El id de la paciente puede ir en --paciente (para todas las grabaciones) o en caso.json: "hablantes": {"<archivo>.json": "speaker_2"}.
Si falta, se deduce (quien hace menos preguntas) y se avisa: confírmalo, porque el id CAMBIA entre grabaciones.
La detección del origen es heurística: marca lo dudoso para que el doctor lo revise; no lo decide por él.

Sale con 0 si los datos firmes permiten nombrar candidatos y 1 si hay que pedir más datos.
"""
import argparse
import importlib.util
import json
import re
import sys
import unicodedata
from pathlib import Path

_spec = importlib.util.spec_from_file_location("revisar_preguntas", Path(__file__).resolve().parent / "revisar_preguntas.py")
revisar_preguntas = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(revisar_preguntas)
LEXICO = revisar_preguntas.lexico_remedios(revisar_preguntas.DB)

FIRMES = {"espontaneo", "abierta", "dos_polos", "observado"}
SIN_TRANSCRIPCION = {"observado", "expediente", "formulario"}
VACIAS = set("""a al algo alguna alguno ante aqui asi como con cual cuando de del donde el ella ellas ellos en entre era es esa ese eso
esta estaba este esto estoy fue ha hace hay la las le les lo los me mi mis mucho muy nada ni no nos o otra otro para pero poco por porque
pues que se si sin sobre su sus tambien te tengo tiene todo tu un una uno usted y ya yo doctor doctora entonces bueno digamos verdad""".split())
SI_NO = re.compile(r"^(si|no|aja|ajam|claro|asi es|exacto|correcto)( (si|no|doctor|doctora|senor|claro))*$")


def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", s)).strip()


def palabras_clave(texto, minimo=5):
    return {w for w in norm(texto).split() if len(w) >= minimo and w not in VACIAS}


def cargar_transcripcion(path):
    """Acepta el JSON de Voxtral ({segments: [...]}) o el de tools/transcribe.py ([{offset, segments}])."""
    data = json.load(open(path, encoding="utf-8"))
    partes = data if isinstance(data, list) else [data]
    segs = []
    for parte in partes:
        off = parte.get("offset", 0) if isinstance(parte, dict) else 0
        for s in parte.get("segments") or [{"text": parte.get("text", "")}]:
            segs.append({"t": s.get("start", 0) + off, "fin": s.get("end", 0) + off, "habla": s.get("speaker_id"),
                         "texto": s.get("text", ""), "n": norm(s.get("text", ""))})
    return segs


def deducir_paciente(segs):
    hablan = {}
    for s in segs:
        if s["habla"]:
            h = hablan.setdefault(s["habla"], [0, 0])
            h[0] += len(s["n"].split())
            h[1] += s["texto"].count("?")
    if len(hablan) < 2:
        return next(iter(hablan), None)
    dos = sorted(hablan, key=lambda k: -hablan[k][0])[:2]
    return min(dos, key=lambda k: hablan[k][1] / max(hablan[k][0], 1))


def mmss(t):
    return f"{int(t) // 60:02d}:{int(t) % 60:02d}"


def ubicar(cita, grabaciones, archivo=None):
    """Busca la cita (palabras completas): primero en la voz de la paciente, luego en la del doctor.
    Si el síntoma dice de qué `archivo` viene, solo busca ahí. Devuelve (estado, archivo, índice)."""
    c = norm(cita)
    if not c:
        return "SIN CITA", None, None
    if archivo and archivo not in grabaciones:
        return "SIN CITA", None, None
    donde = {archivo: grabaciones[archivo]} if archivo else grabaciones
    for nombre, (segs, pac) in donde.items():
        voz = [i for i, s in enumerate(segs) if s["habla"] == pac or pac is None]
        texto, inicios = " ", []
        for i in voz:
            inicios.append((len(texto), i))
            texto += segs[i]["n"] + " "
        pos = texto.find(f" {c} ")
        if pos >= 0:
            idx = max(i for p, i in inicios if p <= pos + 1)
            return "OK", nombre, idx
    for nombre, (segs, pac) in donde.items():
        if f" {c} " in " " + " ".join(s["n"] for s in segs if s["habla"] != pac) + " ":
            return "DICHA POR EL DOCTOR", nombre, None
    return "SIN CITA", None, None


NIEGA = re.compile(r"^(\w+ )?no\b(?! si\b)")          # "no…", pero no "no, sí…" (que en México afirma)
# Dos polos: "X o Y" (sin "o sea"), o los dos polos en dos cláusulas ("¿cómo con el frío y cómo con el calor?").
ALTERNATIVAS = re.compile(r"\b\w+ o (?!sea\b)\w+|\by (como|cuando|que tal)\b")


def dichas_antes(segs, hasta, pac, palabras):
    """Palabras clave que la PACIENTE ya había dicho en la grabación antes del segmento `hasta`."""
    if not palabras:
        return set()
    suyas = set()
    for s in segs[:hasta]:
        if s["habla"] == pac:
            suyas |= palabras_clave(s["texto"])
    return palabras & suyas


def insistencia(segs, idx, pac, cita):
    """Un «sí» conseguido al insistir: el doctor preguntó con la palabra, la paciente NEGÓ, el doctor volvió a
    preguntar con la MISMA palabra y entonces ella afirmó. Devuelve la palabra o None.
    No basta con que haya un «no» cerca: tiene que ser la negación de esa misma palabra."""
    t0 = segs[idx]["t"]
    for j in range(max(0, idx - 12), idx):
        s = segs[j]
        if s["habla"] != pac or t0 - s["t"] > 90 or not NIEGA.match(s["n"]):
            continue
        antes = " ".join(segs[k]["n"] for k in range(max(0, j - 3), j) if segs[k]["habla"] != pac)
        despues = " ".join(segs[k]["n"] for k in range(j + 1, idx) if segs[k]["habla"] != pac)
        # Aquí cuentan también palabras cortas ("sed", "frío"): la repregunta suele ser sobre una sola palabra.
        repetida = palabras_clave(cita, 3) & palabras_clave(antes, 3) & palabras_clave(despues, 3)
        if repetida:
            return sorted(repetida)[0]
    return None


def origen_inferido(cita, segs, idx, pac):
    """Mira la pregunta previa del doctor (hasta 3 turnos, 45 s) y la respuesta. Devuelve (origen, motivo) o (None, None)."""
    previos_i = [j for j in range(max(0, idx - 6), idx) if segs[j]["habla"] != pac and segs[idx]["t"] - segs[j]["t"] <= 45][-3:]
    previos = [segs[j] for j in previos_i]
    pregunta = " ".join(s["n"] for s in previos)
    respuesta = segs[idx]["n"]
    if previos and SI_NO.match(respuesta):
        return "cerrada", "la respuesta es solo sí/no"
    comunes = palabras_clave(cita) & palabras_clave(pregunta)
    palabra = insistencia(segs, idx, pac, cita)
    if palabra:
        return "cerrada", f"afirmó «{palabra}» tras haberlo negado y que se le repreguntara (insistencia)"
    alternativas = ALTERNATIVAS.search(pregunta)
    if "por ejemplo" in pregunta:
        # Un menú que recorre el eje ("por ejemplo, mañana, tarde, noche") no induce un polo; uno de una sola opción sí.
        menu = re.split(r"por ejemplo", " ".join(s["texto"].lower() for s in previos), maxsplit=1)[-1]
        opciones = [o for o in re.split(r",| o | y |\?", menu) if o.strip(" .¿?")]
        if len(opciones) < 2 and not alternativas:
            return "cerrada", "la pregunta ofrecía un menú «por ejemplo…» de una sola opción"
        alternativas = True
    # Pregunta abierta que aprueba revisar_preguntas.py ("¿Qué le da miedo?"): nombra el TEMA, no la respuesta. La palabra
    # del tema en la respuesta no la vuelve cerrada; lo que induce es la pregunta de sí/no o de un solo polo.
    ultima = next((s["texto"] for s in reversed(previos) if "?" in s["texto"]), None)
    if ultima and not revisar_preguntas.revisar(ultima, LEXICO):
        return ("dos_polos" if alternativas else "abierta"), None
    # Eco o ampliación: si la paciente ya había dicho esa palabra antes de la pregunta ("me decía que…, cuénteme más"),
    # no la puso el doctor.
    puestas = comunes - dichas_antes(segs, previos_i[0], pac, comunes) if previos_i else comunes
    if puestas and not alternativas:
        return "cerrada", f"la palabra «{sorted(puestas)[0]}» la dijo primero el doctor"
    if puestas and alternativas:
        return "dos_polos", None
    return None, None


def huecos(segs, umbral=60):
    return [(a["fin"], b["t"]) for a, b in zip(segs, segs[1:]) if b["t"] - a["fin"] > umbral]


def regla_de_tres(sintomas):
    niveles = {s.get("nivel") for s in sintomas}
    return {"Nivel 1-2 (mental con contexto o general)": bool(niveles & {1, 2}),
            "Nivel 3 (raro, peculiar)": 3 in niveles,
            "Nivel 4 (particular con modalidad)": 4 in niveles}


def cuenta_firme(s):
    if s["clase"] != "repertorizable" or s["_estado"] not in ("OK", "NO APLICA") or s["_origen"] not in FIRMES:
        return False
    return not (s.get("nivel") == 1 and not s.get("contexto"))


def validar(caso, grabaciones):
    print(f"Caso: {caso.get('paciente', '?')} · {caso.get('consulta', '?')}\n")
    for nombre, (segs, pac) in grabaciones.items():
        hs = huecos(segs)
        print(f"Grabación {nombre}: paciente = {pac or '?'} · {len(segs)} segmentos · "
              + (f"{len(hs)} hueco(s) >60 s: " + ", ".join(f"{mmss(a)}-{mmss(b)}" for a, b in hs) if hs else "sin huecos >60 s"))
    print()
    sintomas = caso["sintomas"]
    for i, s in enumerate(sintomas, 1):
        s.setdefault("id", f"s{i}")
        declarado = s.get("origen")
        if declarado in SIN_TRANSCRIPCION:
            s["_estado"], s["_origen"], motivo = "NO APLICA", declarado, f"fuente: {declarado}"
        else:
            estado, archivo, idx = ubicar(s.get("cita", ""), grabaciones, s.get("archivo"))
            s["_estado"] = estado
            s["_origen"] = declarado or "sin_declarar"
            motivo = ""
            if estado == "OK":
                segs, pac = grabaciones[archivo]
                inferido, porque = origen_inferido(s["cita"], segs, idx, pac)
                if inferido == "cerrada" and s["_origen"] != "cerrada":
                    s["_origen"], motivo = "cerrada", f"bajado a cerrada: {porque}"
                elif s["_origen"] == "sin_declarar":
                    s["_origen"] = inferido or "sin_declarar"
        if s["clase"] == "repertorizable" and s["_estado"] in ("SIN CITA", "DICHA POR EL DOCTOR"):
            s["clase"] = "informativo"
            motivo = (motivo + "; " if motivo else "") + "bajado a informativo"
        if s.get("nivel") == 1 and s["clase"] == "repertorizable" and not s.get("contexto"):
            motivo = (motivo + "; " if motivo else "") + "mental sin contexto: en observación"
        s["_motivo"] = motivo
        firme = "firme" if cuenta_firme(s) else "     "
        print(f"  {s['id']:>4} [{s['_estado']:<19}] {s.get('t', '--:--'):>8}  {s['clase']:<14} N{s.get('nivel') or '-'}  "
              f"{s['_origen']:<12} {firme}  {s['sintoma']}" + (f"\n{'':>8}↳ {motivo}" if motivo else ""))

    firmes = [s for s in sintomas if cuenta_firme(s)]
    tres = regla_de_tres(firmes)
    print("\nRegla de los Tres (solo datos firmes):")
    for k, v in tres.items():
        print(f"  {'✔' if v else '✘'} {k}")
    sin_declarar = sum(s["_origen"] == "sin_declarar" for s in sintomas)
    if sin_declarar:
        print(f"\n⚠ {sin_declarar} síntoma(s) sin `origen` declarado: no cuentan como firmes. Declara espontaneo/abierta/dos_polos/"
              "cerrada/observado.")

    if caso.get("candidatos"):
        por_id = {s["id"]: s for s in sintomas}
        print("\nPor candidato (apoyo declarado en \"candidatos\"):")
        for remedio, ids in caso["candidatos"].items():
            apoyo = [por_id[i] for i in ids if i in por_id]
            faltan = [i for i in ids if i not in por_id]
            fir = [s for s in apoyo if cuenta_firme(s)]
            ind = [s for s in apoyo if s["_origen"] == "cerrada"]
            sin = [s for s in apoyo if s["_estado"] in ("SIN CITA", "DICHA POR EL DOCTOR")]
            cumple = all(regla_de_tres(fir).values())
            if not cumple:
                tope = "🔴 (no cumple la Regla de los Tres con datos firmes)"
            elif len(ind) + len(sin) >= len(apoyo) / 2:
                tope = "🟡 (la mitad o más del apoyo es inducido o sin cita)"
            else:
                tope = "🟢 posible"
            print(f"  {remedio}: {len(apoyo)} apoyos · {len(fir)} firmes · {len(ind)} inducidos · {len(sin)} sin cita → máximo {tope}"
                  + (f" · ids inexistentes: {', '.join(faltan)}" if faltan else ""))

    listo = all(tres.values())
    print("\n→", "Se pueden nombrar candidatos." if listo else "🔴 Pedir más datos antes de nombrar un remedio.")
    return listo


def caso_validado(caso):
    """El caso con el veredicto del validador escrito en cada síntoma, para que los rubricadores y el abogado lean
    EXACTAMENTE lo que el validador decidió (no el origen que declaró el depurador)."""
    # "candidatos" NO se copia: este archivo lo leen los rubricadores, que deben seguir ciegos a los remedios
    # (auditoría 2026-10-27, H3). El resumen por candidato ya sale en pantalla.
    salida = {k: v for k, v in caso.items() if k not in ("sintomas", "candidatos")}
    salida["validado"] = {"por": "validar_caso.py", "firmes": sum(cuenta_firme(s) for s in caso["sintomas"])}
    salida["sintomas"] = []
    for s in caso["sintomas"]:
        limpio = {k: v for k, v in s.items() if not k.startswith("_")}
        limpio["origen_declarado"] = s.get("origen_declarado", s.get("origen"))
        limpio["origen"] = s["_origen"]
        limpio["estado_cita"] = s["_estado"]
        limpio["firme"] = cuenta_firme(s)
        if s.get("_motivo"):
            limpio["motivo_validador"] = s["_motivo"]
        salida["sintomas"].append(limpio)
    return salida


def revisar_afirmaciones(afirmaciones, texto):
    print("\nDatos del análisis previo frente a la grabación:")
    for a in afirmaciones:
        patron = a["patron"].replace(",", "").replace(".", "")  # P5: el texto normalizado no lleva puntuación
        hit = re.search(norm(patron) if not re.search(r"[\\()\[\]|?*+]", patron) else patron, texto)
        detalle = f"  («…{hit.group(0)}…»)" if hit else ""
        print(f"  [{'aparece' if hit else 'NO está'}] {a['dato']}{detalle}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("caso")
    ap.add_argument("archivos", nargs="+", help="transcripciones JSON y, al final, afirmaciones.json (opcional)")
    ap.add_argument("--paciente", help="id del hablante que es la paciente en todas las grabaciones")
    ap.add_argument("--salida", help="dónde escribir el caso validado (por omisión: caso_validado.json junto a caso.json)")
    a = ap.parse_args()
    caso = json.load(open(a.caso, encoding="utf-8"))
    afirmaciones, grabaciones = None, {}
    for f in a.archivos:
        data = json.load(open(f, encoding="utf-8"))
        if isinstance(data, list) and data and isinstance(data[0], dict) and "patron" in data[0]:
            afirmaciones = data
            continue
        segs = cargar_transcripcion(f)
        nombre = Path(f).name
        pac = a.paciente or caso.get("hablantes", {}).get(nombre)
        if not pac and any(s["habla"] for s in segs):
            pac = deducir_paciente(segs)
            print(f"⚠ {nombre}: paciente deducida = {pac} (quien hace menos preguntas). Confírmalo con extraer_transcripcion.py.")
        grabaciones[nombre] = (segs, pac)
    listo = validar(caso, grabaciones)
    salida = Path(a.salida) if a.salida else Path(a.caso).with_name("caso_validado.json")
    json.dump(caso_validado(caso), open(salida, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nCaso validado → {salida} (los rubricadores y el abogado leen ESTE archivo; caso.json no se toca)")
    if afirmaciones:
        revisar_afirmaciones(afirmaciones, " ".join(s["n"] for segs, _ in grabaciones.values() for s in segs))
    sys.exit(0 if listo else 1)
