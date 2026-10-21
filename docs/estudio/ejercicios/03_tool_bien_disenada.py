"""Módulo 3 · Una tool mal diseñada frente a una bien diseñada, sin API.

Corre:  python3 03_tool_bien_disenada.py
"""
ESTACIONES = {
    "Insurgentes": ["Línea 1"],
    "Insurgentes Sur": ["Línea 12"],
    "Pantitlán": ["Línea 1", "Línea 5", "Línea 9", "Línea A"],
}
ENTRADAS = {("Pantitlán", "Línea A"): 910_000, ("Insurgentes", "Línea 1"): 1_050_000}


def ejecutar_sql(query):
    """MAL: demasiado amplia. El modelo puede intentar cualquier cosa (y romperla)."""
    return "error: syntax error near 'selct'"  # el modelo no aprende nada útil de esto


def afluencia_metro(estacion, linea=None):
    """BIEN: una intención clara. Los errores le dicen al modelo QUÉ hacer para corregirse."""
    coincidencias = [e for e in ESTACIONES if estacion.lower() in e.lower()]
    if not coincidencias:
        return {"error": f"No existe «{estacion}». Usa buscar_estacion_metro para ver los nombres exactos."}
    if len(coincidencias) > 1:
        return {"error": f"«{estacion}» coincide con varias estaciones: {', '.join(coincidencias)}. "
                         "Repite con el nombre exacto."}
    nombre = coincidencias[0]
    if linea is None and len(ESTACIONES[nombre]) > 1:
        return {"error": f"{nombre} tiene varias líneas: {', '.join(ESTACIONES[nombre])}. Indica `linea`."}
    linea = linea or ESTACIONES[nombre][0]
    return {"estacion": nombre, "linea": linea, "entradas_julio_2026": ENTRADAS.get((nombre, linea), 0),
            "nota": "afluencia = entradas, no ocupación de trenes"}


if __name__ == "__main__":
    print("Mala  ->", ejecutar_sql("selct * from afluencia"))
    print("Buena (nombre ambiguo)   ->", afluencia_metro("insurgente"))
    print("Buena (falta la línea)   ->", afluencia_metro("Pantitlán"))
    print("Buena (corregido)        ->", afluencia_metro("Pantitlán", "Línea A"))
