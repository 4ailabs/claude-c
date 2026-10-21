# Tool use sin abstracciones

**Ponente:** Carlos Haro (AI Engineer & Technical PM, Santander)

Del token al `tool_result`, y las formas en que se rompe. Agente escrito a mano sobre la API de Claude, sin frameworks.

## Sales con

- Un agente propio que rompes a propósito: historial con `tool_use` huérfano, JSON truncado por `max_tokens`, llamadas paralelas y una llamada válida pero semánticamente peligrosa.
- Cada falla reparada en código.
- La tasa de error de herramientas de tu agente, por categoría y con costo.

## En una frase

Escribir a mano el ciclo que lee lo que el modelo pide, lo ejecuta y responde con un `tool_result`, y medir cuánto falla.

## Lo esencial

- **El modelo propone, la aplicación ejecuta.** El arnés es ese ciclo; un framework solo lo esconde.
- El mismo modelo falla distinto según el proveedor: se mide la tasa de error de tool calls por categoría.
- Hay que romper el agente a propósito (historial con `tool_use` huérfano, JSON truncado, una llamada válida pero peligrosa) y repararlo.

## Qué hay en esta carpeta

| Archivo | Para qué |
|---|---|
| [`notas.md`](notas.md) | Lo que se dijo, en orden, con marcas `[hh:mm:ss]` y las dudas marcadas con (?) |
| [`preguntas.md`](preguntas.md) | Las **tres preguntas** para el ponente, sobre su experiencia (y una reserva) |
| [`tareas.md`](tareas.md) | La consigna, el plan y el avance de la práctica |
| [`claude4aieng/`](claude4aieng) | Repo del ponente ([h1sort/claude4aieng](https://github.com/h1sort/claude4aieng)), rama `paso-0`; **no se versiona aquí** |
| Transcripción | `transcripts/01-tool-use-sin-abstracciones/`, **no se versiona** (lleva voces de asistentes) |

## Para retomarlo

```bash
cd workshops/01-tool-use-sin-abstracciones/claude4aieng
uv run pytest -q                          # 110 pasan, 17 se saltan (pasos 2 a 4 pendientes)
export ANTHROPIC_API_KEY=...              # la escribes tú; necesita créditos
uv run python -m taller.agent             # pregunta: «¿cuántas tarjetas bloqueadas hay?» → 26
```

Siguiente: los `TODO(paso-2)`, `paso-2b`, `paso-3` y `paso-4` de `taller/agent.py` y `taller/tools.py`. La solución de cada uno está en las ramas `paso-N` del repo.

## Estado

- [x] Notas, preguntas y tareas.
- [x] **Paso 1** escrito en `taller/agent.py` (cambio sin commitear en el repo del ponente) y comparado con la solución oficial.
- [ ] Pasos 2, 2b, 3 y 4.
- [ ] Probar el agente con una API key de Anthropic **con créditos**.
- [ ] Hueco sin grabar de 18:04 a 18:08 (se explicaba la solución del ejercicio).

> `uv sync` descarga paquetes; si el Wi-Fi es lento, hazlo antes.

**Para estudiar este tema:** [Módulo 1 · El agente actúa](../../docs/estudio/01-el-agente-actua.md) (y el 6 para medir errores).

Ver también: [guía final](../../docs/guia-final.md) · [conceptos](../../docs/conceptos.md) · [temario](../../docs/temario.md).
