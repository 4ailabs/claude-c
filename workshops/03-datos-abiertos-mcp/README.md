# Datos abiertos over MCP

**Ponente:** Dante Bazaldua (Co-founder & CTO, Spot2)

Claude que consulta fuentes reales.

## Sales con

- Un server FastMCP que expone datos (consulta tipo open data + una acción controlada).
- Conectado a Claude Code.
- Diseño de tools para que el modelo elija bien.

## En una frase

Un servidor MCP con datos abiertos del Metro de la CDMX, conectado a Claude Code, con tools bien diseñadas y controles en el código.

## Lo esencial

- Una tool es una función que el modelo pide y tu código ejecuta; MCP es el estándar para publicarlas.
- Se diseña **por intención**, con respuestas cortas y errores que enseñan.
- Si la tool escribe, los controles van **en el código** (validación, idempotencia, aprobación humana), no en el prompt.
- Se mide con una evaluación de 10 preguntas.

## Qué hay en esta carpeta

| Archivo | Para qué |
|---|---|
| [`notas.md`](notas.md) | Lo que se dijo, en orden, con marcas `[hh:mm:ss]` y las dudas marcadas con (?) |
| [`preguntas.md`](preguntas.md) | Las **tres preguntas** para el ponente, sobre su experiencia (y una reserva) |
| [`tareas.md`](tareas.md) | La consigna, el plan y el avance de la práctica |
| [`claude-mcp-ibero-2026/`](claude-mcp-ibero-2026) | Repo del ponente ([danteese/claude-mcp-ibero-2026](https://github.com/danteese/claude-mcp-ibero-2026)); **no se versiona aquí** |
| PDF de la sesión | `https://stdout.mx/claude4aieng/datos-mcp-ibero.pdf` |
| Transcripción | `transcripts/03-datos-abiertos-mcp/`, **no se versiona** (lleva voces de asistentes) |

## Para retomarlo

```bash
# Terminal 1: el servidor (se queda corriendo)
cd workshops/03-datos-abiertos-mcp/claude-mcp-ibero-2026 && uv run servidor.py

# Terminal 2: Claude Code dentro del repo
cd workshops/03-datos-abiertos-mcp/claude-mcp-ibero-2026 && claude
```

En Claude Code: `/mcp` → `cdmx` → **Enable** (en esta Mac quedó desactivado en la ruta vieja; al abrir desde la ruta nueva pedirá confirmar). Debe mostrar **8 tools**.
Pregunta de prueba: «¿Cuánta gente entró a Pantitlán en julio de 2026?» → **4,623,233**.
Por paso: `cp pasos/0N_*.py servidor.py` → reiniciar el servidor → `/mcp → cdmx → Reconnect` → `uv run verificar.py N`.

## Estado

- [x] Notas, preguntas y tareas.
- [x] Datos preparados (`preparar.py`, 38,804 filas) y `verificar.py` en verde.
- [x] **Pasos 2, 3 y 4** copiados a `servidor.py` y comprobados: 8 tools, un resource y un prompt.
- [ ] Conectar `cdmx` en Claude Code y probar las preguntas de cada paso.
- [ ] `uv run evaluar.py` (no se ha corrido; **gasta cuota de Claude**).

> En esta carpeta hay un `server.py` suelto (un servidor MCP mínimo) que **no pertenece al repo del ponente** ni está versionado.

**Para estudiar este tema:** [Módulo 3 · MCP y diseño de tools](../../docs/estudio/03-mcp-y-diseno-de-tools.md) y el [4 · Controles y seguridad](../../docs/estudio/04-controles-y-seguridad.md).

Ver también: [guía final](../../docs/guia-final.md) · [conceptos](../../docs/conceptos.md) · [temario](../../docs/temario.md).
