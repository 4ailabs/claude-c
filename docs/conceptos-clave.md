# Ocho conceptos para no perderse

Diapositiva de cierre del evento ("Lo que escuchaste hoy", Claude Community, claude.rich, lámina 39).

Flujo: **Contexto** (con resumen) → **Claude** → `tool_use` → **tu código** → **MCP** → datos abiertos / mundo físico.
El `tool_result` regresa al contexto: es **el loop, hasta terminar la tarea**. Al lado: subagentes y evals.

| # | Workshop | Concepto | Definición en la lámina |
|---|---|---|---|
| 1 | 1 | Tool use | Claude no ejecuta nada: pide una herramienta (`tool_use`) y tu código le regresa el `tool_result`. |
| 2 | 1 | El loop | Un agente es eso, repetido hasta terminar la tarea. Y ahí es donde se rompe. |
| 3 | 2 | Contexto | Todo lo que Claude ve en una llamada. Cabe un millón de tokens; lo que importa es qué metes. |
| 4 | 2 | Compactación | Resumir el historial para seguir trabajando, y cargar tools solo cuando hacen falta. |
| 5 | 3 y 4 | MCP | Model Context Protocol: el estándar para conectar datos y herramientas a Claude. Un server, muchos clientes. |
| 6 | 4 | Tools seguras | Cuando una acción mueve algo en el mundo físico, la tool decide qué se permite y qué no. |
| 7 | 5 | Subagentes | Un orquestador divide la tarea y delega en otros agentes, cada uno con sus tools, permisos y guardrails. |
| 8 | 5 | Evals | Casos y métricas para saber si tu agente mejora o empeora. Y un juez LLM para lo que no mide una regla. |
