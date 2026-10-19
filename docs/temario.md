# Temario

Tomado de la página del evento.

## Line-up

- Carlos Haro: AI Engineer & Technical Product Manager, Santander
- Alejandro Martínez: Sr Software Engineer, Platzi
- Dante Bazaldua: Co-founder & CTO, Spot2
- Jonathan Olvera: Founder & CTO, Hiveflow
- Jésica Tapia: NLP & AI Policy Specialist, UNESCO
- Rich Lira: Claude Community Ambassador

## Workshop 1 · Tool use sin abstracciones · Carlos Haro

Del token al `tool_result`, y las formas en que se rompe. Escribes a mano un
agente sobre la API de Claude, sin frameworks, y lo rompes a propósito: historial
con `tool_use` huérfano, JSON truncado por `max_tokens`, llamadas paralelas y una
llamada válida pero semánticamente peligrosa. Reparas cada falla en código y sales
midiendo la tasa de error de herramientas de tu propio agente, por categoría y con
costo por… *(el texto de la página llega cortado aquí)*.

## Workshop 2 · Context engineering · Alejandro Martínez

Compactación y descubrimiento dinámico de contexto y tools. Sales con un agente
construido con Pydantic AI que resume su contexto para continuar una tarea, busca
y carga información de archivos en disco, y carga las herramientas que necesita
cuando las necesita. Comparamos qué información conserva y cuánto contexto usa.

## Workshop 3 · Datos abiertos over MCP · Dante Bazaldua

Claude que consulta fuentes reales. Sales con un server FastMCP que expone datos
(consulta tipo open data + una acción controlada), conectado a Claude Code, y con
el diseño de tools para que el modelo elija bien y no… *(el texto llega cortado aquí)*.

## Workshop 4 · Physical AI + MCP + Swarm Protocol · Jonathan Olvera

Claude operando hardware real, de un agente a un enjambre. Construyes tu propio
MCP server para conectar Claude Code a hardware real: lees sensores, accionas
dispositivos desde una conversación y aprendes a diseñar tools seguras cuando las
acciones tienen consecuencias físicas. Cerramos con Swarm Protocol, convirtiendo
ese agente en un enjambre coordinado operando el mundo físico. Sales con tu propio
MCP server controlando hardware y el repo open source para replicarlo. El hardware
lo ponen los organizadores.

## Workshop 5 · Del agente al equipo · Jésica Tapia

Orquestación, guardrails y evaluaciones con Claude. Sales con un sistema
multiagente construido con la API de Claude: un orquestador que divide la tarea y
delega en subagentes especializados, cada uno con sus propias tools, permisos y
guardrails. Se pone a prueba con evaluaciones: un set de casos, métricas por
agente y del sistema completo, y un juez LLM para lo que no se puede medir con
reglas. Qué falla cuando un agente trabaja solo, qué falla cuando se coordinan
varios, y cómo detectarlo antes de que llegue a producción.
