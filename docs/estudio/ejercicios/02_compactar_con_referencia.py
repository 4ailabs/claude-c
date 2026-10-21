"""Módulo 2 · Compactar sin y con referencia, sin API.

Un historial largo esconde un dato (un número de serie). Se "compacta" de dos formas y se ve qué se pierde.
Corre:  python3 02_compactar_con_referencia.py
"""
import json
import tempfile
from pathlib import Path

historial = [{"n": i, "texto": f"mensaje {i}: conversación normal sobre el pedido"} for i in range(1, 201)]
historial[136]["texto"] = "mensaje 137: el serial dañado es AO-2048-009"


def resumir(mensajes):
    """Un 'resumen' ingenuo: conserva el tema, no los detalles (como cualquier resumen)."""
    return f"Resumen: {len(mensajes)} mensajes sobre un pedido con equipos dañados."


def buscar(ruta, texto):  # como search_file / grep: devuelve solo las líneas que coinciden
    return [l.strip() for l in Path(ruta).read_text().splitlines() if texto.lower() in l.lower()]


original = "\n".join(json.dumps(m, ensure_ascii=False) for m in historial)
print(f"Historial original: {len(original):,} caracteres\n")

# A) Sin referencia: solo queda el resumen.
sin_ref = resumir(historial)
print("A) SIN referencia →", sin_ref)
print("   ¿Sabe el serial? ", "AO-2048-009" in sin_ref, f"({len(sin_ref)} caracteres)\n")

# B) Con referencia: el resumen + un puntero al original guardado en disco.
ruta = Path(tempfile.mkdtemp()) / "historial.jsonl"
ruta.write_text(original)
con_ref = resumir(historial) + f" Historial completo en: {ruta.name}. Si faltan detalles, búscalos ahí."
print("B) CON referencia →", con_ref)
print("   ¿Sabe el serial en el contexto? ", "AO-2048-009" in con_ref, f"({len(con_ref)} caracteres)")
encontrado = buscar(ruta, "serial")
print("   Pero puede BUSCARLO en el archivo:", encontrado[0][:70], "...")
print(f"   Coste: la búsqueda devolvió {sum(len(l) for l in encontrado)} caracteres, no los {len(original):,}.")
