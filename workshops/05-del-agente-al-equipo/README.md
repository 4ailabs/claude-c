# Del agente al equipo

**Ponente:** Jésica Tapia (NLP & AI Policy Specialist, UNESCO)

Orquestación, guardrails y evaluaciones con Claude.

## Sales con

- Un sistema multiagente con la API de Claude: un orquestador que divide la tarea y delega en subagentes con sus propias tools, permisos y guardrails.
- Evaluaciones: set de casos, métricas por agente y del sistema completo, y un juez LLM para lo que no se mide con reglas.
- Qué falla cuando un agente trabaja solo, qué falla cuando se coordinan varios, y cómo detectarlo antes de producción.

## En una frase

Auditar un sistema multiagente que evalúa CVs: barandillas, sesgo, bitácoras con hash y regulación.

## Lo esencial

- El sesgo no viene solo de los datos, también de los hábitos humanos.
- Barandillas a la entrada y a la salida; el sistema **no recomienda** a quién contratar.
- Se prueba comparando una corrida ingenua con una protegida y con pares de CVs idénticos.
- Las bitácoras llevan hash; queda una tensión sin resolver entre guardar todo y proteger los datos personales.

## Qué hay en esta carpeta

| Archivo | Para qué |
|---|---|
| [`notas.md`](notas.md) | Lo que se dijo, en orden, con marcas `[hh:mm:ss]` y las dudas marcadas con (?) |
| [`preguntas.md`](preguntas.md) | Las **tres preguntas** para el ponente, sobre su experiencia (y una reserva) |
| [`tareas.md`](tareas.md) | La consigna, el plan y el avance de la práctica |
| *(repo del ponente)* | **Falta el enlace**: aparece con un QR en sus diapositivas; sin clonar |
| Transcripción | `transcripts/05-del-agente-al-equipo/`, **no se versiona** (lleva voces de asistentes) |

## Para retomarlo

1. Conseguir el enlace del repositorio de evaluación multiagente (en la diapositiva del QR) y clonarlo aquí:
   `git clone <enlace> workshops/05-del-agente-al-equipo/<nombre>`
   y añadir su ruta a `.git/info/exclude` para no versionar el código de otra persona.
2. Correrlo primero en **modo simulación** (no gasta créditos). Con API key hace llamadas reales y avisa de un cálculo aproximado.
3. Hacer los ejercicios: pares de CVs que solo cambian hombre/mujer, otros idiomas y una señal indirecta (universidad pública o privada).

## Estado

- [x] Notas, preguntas y tareas.
- [ ] **Enlace del repo y clonado.**
- [ ] Correr en simulación y hacer los ejercicios de sesgo.

> En la grabación de este workshop, los primeros 9 minutos son el cierre del workshop 4 (el video del enjambre); está resumido en las notas del workshop 4.

**Para estudiar este tema:** [Módulo 6 · Evaluar y auditar](../../docs/estudio/06-evaluar-y-auditar.md) y el [4 · Controles y seguridad](../../docs/estudio/04-controles-y-seguridad.md).

Ver también: [guía final](../../docs/guia-final.md) · [conceptos](../../docs/conceptos.md) · [temario](../../docs/temario.md).
