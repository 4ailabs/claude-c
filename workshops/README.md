# Workshops

Los cinco workshops del evento, en el orden en que se dieron. Cada carpeta es una portada con el estado real y los comandos para retomarlo.

| # | Workshop | Ponente | Notas | Código del ponente | Siguiente paso |
|---|---|---|---|---|---|
| 1 | [Tool use sin abstracciones](01-tool-use-sin-abstracciones) | Carlos Haro (Santander) | ✅ | `claude4aieng/` · paso 1 hecho | Pasos 2 a 4; probar con API key con créditos |
| 2 | [Context engineering](02-context-engineering) | Alejandro Martínez (Platzi) | ✅ | `context-engineering-workshop/` · paso 2 hecho | Pasos 3 a 5; probar el chat |
| 3 | [Datos abiertos over MCP](03-datos-abiertos-mcp) | Dante Bazaldua (Spot2) | ✅ | `claude-mcp-ibero-2026/` · pasos 2 a 4 copiados y verificados | Conectar `cdmx` en Claude Code y probar |
| 4 | [Physical AI + MCP + Swarm Protocol](04-physical-ai-mcp-swarm) | Jonathan Olvera (Hiveflow) | ✅ | `physical-ai-workshop/` · clonado, sin ejecutar | Cuenta de Hiveflow y API key (la creas tú) |
| 5 | [Del agente al equipo](05-del-agente-al-equipo) | Jésica Tapia (UNESCO) | ✅ | *falta el enlace del repo* | Conseguir el repo; correr en simulación |

## Qué tiene cada carpeta

| Archivo | Para qué |
|---|---|
| `README.md` | Portada: en una frase, lo esencial, estado y cómo retomarlo |
| `notas.md` | Lo que se dijo, en orden, con marcas de tiempo y dudas marcadas con (?) |
| `preguntas.md` | Tres preguntas para el ponente (sobre su experiencia), más una reserva |
| `tareas.md` | La consigna, el plan y el avance de la práctica |
| *repo del ponente* | Código clonado; no se versiona aquí (otra persona lo mantiene) |

Las transcripciones viven en `transcripts/` y las grabaciones en `recordings/`; ninguna se versiona.

## Por dónde empezar

1. **Para estudiar:** la [ruta de estudio](../docs/estudio/README.md), con los temas de las cinco clases juntos, ordenados y con ejercicios.
2. Para repasar: la [guía final](../docs/guia-final.md) y el [mapa de conceptos](../docs/conceptos.md).
3. Para ver cada clase por separado, sigue el orden 1 → 5 (tool use → contexto → MCP → mundo físico y enjambres → auditoría).
4. Antes de gastar créditos, usa lo que no los consume: las pruebas locales de los workshops 1 y 2, `verificar.py` del 3 y el modo simulación del 5.

## Qué hace falta de tu parte

- Una **API key de Anthropic con créditos** para los workshops 1 y 2 (la escribes tú en un `.env` o en la terminal).
- La cuenta de **Hiveflow** y su API key para el workshop 4.
- El **enlace del repo** del workshop 5.
