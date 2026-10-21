"""Módulo 6 · Auditar sesgo con un par de CVs idénticos. Sin API (juguete).

Un "evaluador" con un sesgo escondido: penaliza la pausa laboral. La prueba del par lo delata.
Corre:  python3 06_par_de_cvs.py
"""


def evaluar_ingenuo(cv):
    puntos = 50 + 10 * cv["anios_experiencia"] + 5 * len(cv["habilidades"])
    if cv["pausa_laboral"]:
        puntos -= 15            # sesgo escondido: castiga la pausa (a menudo, por cuidados)
    return puntos


def evaluar_protegido(cv):
    """Barandilla: los atributos protegidos o sus proxies no entran al puntaje."""
    sin_proxies = {k: v for k, v in cv.items() if k not in ("pausa_laboral", "genero", "estado_civil")}
    return 50 + 10 * sin_proxies["anios_experiencia"] + 5 * len(sin_proxies["habilidades"])


base = {"anios_experiencia": 8, "habilidades": ["python", "sql", "datos"], "genero": "mujer",
        "estado_civil": "casada", "pausa_laboral": False}
par = {**base, "pausa_laboral": True}          # IDÉNTICO, salvo la pausa

print("Par de CVs idénticos salvo la pausa laboral\n")
print(f"  Ingenuo   : {evaluar_ingenuo(base)} vs {evaluar_ingenuo(par)}  → diferencia {evaluar_ingenuo(base) - evaluar_ingenuo(par)}")
print(f"  Protegido : {evaluar_protegido(base)} vs {evaluar_protegido(par)}  → diferencia {evaluar_protegido(base) - evaluar_protegido(par)}")
print("\nSi dos CVs iguales reciben puntajes distintos, la diferencia es sesgo.")
