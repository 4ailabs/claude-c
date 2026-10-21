"""Módulo 1 · Un arnés mínimo, sin API.

Un "modelo" falso pide una herramienta; tu arnés la ejecuta y devuelve el resultado.
Corre:  python3 01_mini_arnes.py
"""

TARJETAS = [{"id": 1, "estado": "bloqueada"}, {"id": 2, "estado": "activa"}, {"id": 3, "estado": "bloqueada"}]


def contar_tarjetas(estado):
    return sum(1 for t in TARJETAS if t["estado"] == estado)


HERRAMIENTAS = {"contar_tarjetas": contar_tarjetas}


def modelo_falso(mensajes):
    """Hace lo que haría Claude: primero PIDE la herramienta; cuando ve el resultado, responde."""
    ultimo = mensajes[-1]
    if ultimo["role"] == "user" and isinstance(ultimo["content"], str):
        return {"stop_reason": "tool_use", "content": [
            {"type": "tool_use", "id": "toolu_01", "name": "contar_tarjetas", "input": {"estado": "bloqueada"}}]}
    resultado = ultimo["content"][0]["content"]
    return {"stop_reason": "end_turn", "content": [{"type": "text", "text": f"Hay {resultado} tarjetas bloqueadas."}]}


def validar_historial(mensajes):
    """La API real exige un tool_result por CADA tool_use, en el mensaje de usuario siguiente."""
    for i, m in enumerate(mensajes):
        if m["role"] != "assistant":
            continue
        ids = [b["id"] for b in m["content"] if b["type"] == "tool_use"]
        siguiente = mensajes[i + 1]["content"] if i + 1 < len(mensajes) else []
        hechos = {b["tool_use_id"] for b in siguiente if isinstance(siguiente, list) and b["type"] == "tool_result"}
        faltan = [x for x in ids if x not in hechos]
        if faltan:
            raise ValueError(f"tool_use sin tool_result: {faltan}  (la API real respondería 400)")


def agente(pregunta, olvidar_resultado=False):
    mensajes = [{"role": "user", "content": pregunta}]
    for _ in range(5):
        validar_historial(mensajes)
        respuesta = modelo_falso(mensajes)
        mensajes.append({"role": "assistant", "content": respuesta["content"]})
        if respuesta["stop_reason"] != "tool_use":
            return respuesta["content"][0]["text"]
        resultados = []
        for bloque in respuesta["content"]:
            if bloque["type"] == "tool_use":  # el modelo PROPONE; este código EJECUTA
                salida = HERRAMIENTAS[bloque["name"]](**bloque["input"])
                resultados.append({"type": "tool_result", "tool_use_id": bloque["id"], "content": str(salida)})
        if not olvidar_resultado:
            mensajes.append({"role": "user", "content": resultados})
    return "(se acabaron los turnos)"


if __name__ == "__main__":
    print("1) Arnés completo:      ", agente("¿Cuántas tarjetas bloqueadas hay?"))
    try:
        agente("¿Cuántas tarjetas bloqueadas hay?", olvidar_resultado=True)
    except ValueError as error:
        print("2) Olvidando el result: ", error)
