"""Módulo 5 · Umbrales, humano en el loop y bitácora con hash. Sin API.

Corre:  python3 05_umbral_y_bitacora.py
"""
import hashlib
import json

CRITERIOS_EMERGENCIA = 2   # cuántas señales independientes hacen falta antes de molestar a un humano


def revisar(lecturas):
    """Cuenta señales; solo con 2 o más se pide la confirmación de una persona."""
    senales = [k for k, v in lecturas.items() if v]
    if len(senales) >= CRITERIOS_EMERGENCIA:
        return "ESCALAR_A_HUMANO", senales
    return "SEGUIR_OBSERVANDO", senales


def agregar(bitacora, evento):
    """Cada entrada incluye el hash de la anterior: si alguien edita el pasado, la cadena se rompe."""
    previo = bitacora[-1]["hash"] if bitacora else "0" * 8
    cuerpo = json.dumps(evento, sort_keys=True)
    bitacora.append({"evento": evento, "hash": hashlib.sha256((previo + cuerpo).encode()).hexdigest()[:8]})


def verificar(bitacora):
    previo = "0" * 8
    for i, e in enumerate(bitacora):
        esperado = hashlib.sha256((previo + json.dumps(e["evento"], sort_keys=True)).encode()).hexdigest()[:8]
        if esperado != e["hash"]:
            return f"MANIPULADA en la entrada {i}"
        previo = e["hash"]
    return "íntegra"


if __name__ == "__main__":
    bitacora = []
    casos = [{"humo": True, "puerta_abierta": False, "temperatura_alta": False},
             {"humo": True, "puerta_abierta": True, "temperatura_alta": False}]
    for caso in casos:
        decision, senales = revisar(caso)
        agregar(bitacora, {"senales": senales, "decision": decision})
        print(f"{len(senales)} señal(es) {senales} -> {decision}")
    print("Bitácora:", verificar(bitacora))
    bitacora[0]["evento"]["decision"] = "ESCALAR_A_HUMANO"   # alguien 'arregla' el pasado
    print("Después de editar una entrada:", verificar(bitacora))
