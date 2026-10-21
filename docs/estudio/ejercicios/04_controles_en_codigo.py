"""Módulo 4 · Los controles van en el CÓDIGO, no en el prompt. Sin API.

Una tool que escribe: esquema cerrado, idempotencia, tope por hora y aprobación humana.
Corre:  python3 04_controles_en_codigo.py
"""
import hashlib

REPORTES = {}      # "base de datos": clave idempotente -> folio
HISTORIAL_HORA = []  # marcas de tiempo simuladas
TOPE_POR_HORA = 3


def registrar_reporte(estacion, descripcion, aprobar):
    # 1) Esquema cerrado: aunque el modelo "quiera", el código rechaza lo que no cumple.
    if not isinstance(descripcion, str) or not 10 <= len(descripcion) <= 500:
        return "RECHAZADO: la descripción debe tener entre 10 y 500 caracteres."
    # 2) Aprobación humana: nada se escribe sin el sí de una persona.
    if not aprobar(f"¿Registro este reporte en {estacion}? «{descripcion}»"):
        return "RECHAZADO: la persona no lo aprobó."
    # 3) Idempotencia: repetir la llamada NO duplica el efecto; devuelve el mismo folio.
    clave = hashlib.sha256(f"{estacion}|{descripcion}".encode()).hexdigest()
    if clave in REPORTES:
        return f"Ya existía: {REPORTES[clave]} (no se duplicó)"
    # 4) Tope: un modelo que se cicla no puede inundar el sistema.
    if len(HISTORIAL_HORA) >= TOPE_POR_HORA:
        return "RECHAZADO: tope de reportes por hora alcanzado."
    folio = f"CDMX{len(REPORTES) + 1:05d}"
    REPORTES[clave] = folio
    HISTORIAL_HORA.append(1)
    return f"Registrado: {folio}"


if __name__ == "__main__":
    si = lambda pregunta: True
    no = lambda pregunta: False
    texto = "El elevador de Pantitlán, Línea A, no funciona"
    print("1) Corto           ->", registrar_reporte("Pantitlán", "roto", si))
    print("2) Sin aprobación  ->", registrar_reporte("Pantitlán", texto, no))
    print("3) Aprobado        ->", registrar_reporte("Pantitlán", texto, si))
    print("4) Repetido        ->", registrar_reporte("Pantitlán", texto, si))
    for i in range(4):
        r = registrar_reporte("Pantitlán", f"Otro problema distinto número {i} en la estación", si)
    print("5) Ciclo de 4 más  ->", r)
