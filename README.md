# Claude for AI Engineering — Ciudad de México

Repositorio del evento de la comunidad Claude dedicado a AI Engineering, en la
Universidad Iberoamericana (Ciudad de México). Primer evento de las dos semanas
de Claude en CDMX y el más técnico de la serie: una tarde con cinco workshops
hands-on, de sistemas y no de prompts sueltos.

> Tool use, context engineering, MCP, hardware real, orquestación y evals: lo que
> separa un demo bonito de infraestructura que aguanta tráfico real.

## Antes de llegar

Laptop con todo instalado y **probado**:

- Git
- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- [Claude Code](https://claude.com/claude-code)

Verifica con `./tools/check-setup.sh`.

## Agenda

| Hora | Qué |
|---|---|
| 4:30 PM | Registro y setup |
| 5:00 PM | Bienvenida: Rich Lira y Alejandro Anaya (vicerrector, Universidad Iberoamericana) |
| 5:10 PM | State of Claude, con Rich |
| 5:20 PM | Arrancan los cinco workshops |
| 9:05 PM | Cierre y networking hasta las 9:30 PM |

## Workshops

| # | Workshop | Ponente | Carpeta |
|---|---|---|---|
| 1 | Tool use sin abstracciones | Carlos Haro (Santander) | [workshops/01-tool-use-sin-abstracciones](workshops/01-tool-use-sin-abstracciones) |
| 2 | Context engineering | Alejandro Martínez (Platzi) | [workshops/02-context-engineering](workshops/02-context-engineering) |
| 3 | Datos abiertos over MCP | Dante Bazaldua (Spot2) | [workshops/03-datos-abiertos-mcp](workshops/03-datos-abiertos-mcp) |
| 4 | Physical AI + MCP + Swarm Protocol | Jonathan Olvera (Hiveflow) | [workshops/04-physical-ai-mcp-swarm](workshops/04-physical-ai-mcp-swarm) |
| 5 | Del agente al equipo | Jésica Tapia (UNESCO) | [workshops/05-del-agente-al-equipo](workshops/05-del-agente-al-equipo) |

Más detalle del temario en [docs/temario.md](docs/temario.md).

## Grabación y transcripción

Cada sesión se graba y se transcribe con la API de Voxtral de Mistral.
Las grabaciones viven en `recordings/` (ignoradas por git) y las transcripciones
en `transcripts/<workshop>/`. Ver [docs/transcripcion.md](docs/transcripcion.md).

```bash
cp .env.example .env        # pon MISTRAL_API_KEY
uv run tools/transcribe.py recordings/01.m4a \
  --out transcripts/01-tool-use-sin-abstracciones/sesion.md
```
