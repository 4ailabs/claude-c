# Tool use sin abstracciones

**Ponente:** Carlos Haro (AI Engineer & Technical PM, Santander)

Del token al `tool_result`, y las formas en que se rompe. Agente escrito a mano sobre la API de Claude, sin frameworks.

## Sales con

- Un agente propio que rompes a propósito: historial con `tool_use` huérfano, JSON truncado por `max_tokens`, llamadas paralelas y una llamada válida pero semánticamente peligrosa.
- Cada falla reparada en código.
- La tasa de error de herramientas de tu agente, por categoría y con costo.

## Contenido del repo

- `README.md`: esta guía
- `notas.md`: notas de la sesión
- La transcripción va en [`transcripts/01-tool-use-sin-abstracciones/`](../../transcripts/01-tool-use-sin-abstracciones)

> Código y ejercicios: se agregan durante o después del workshop.
