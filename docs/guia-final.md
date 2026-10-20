# Guía final · Claude for AI Engineering · CDMX

Una tarde de cinco workshops técnicos (19 de octubre de 2026, Universidad Iberoamericana, Ciudad de México). Esta guía junta lo esencial para estudiarlo después, en orden y sin tener que releer cinco transcripciones.

- **Para empezar:** lee "Las ideas que más importan" y la "Ruta de estudio".
- **Para profundizar:** cada workshop tiene sus notas con marcas de tiempo en `workshops/NN-*/notas.md`.
- **Para consultar un concepto:** [conceptos.md](conceptos.md), con 23 conceptos ordenados de lo básico a lo avanzado.

## La tesis del evento

> **El modelo propone, la aplicación ejecuta, y eso se mide.**

Todo lo demás son consecuencias: cómo se ejecuta bien, qué contexto ve el agente, cómo se conecta con el mundo, qué pasa cuando actúa en lo físico o con otros agentes, y cómo se audita.

## Los cinco workshops

| # | Workshop | Ponente | En una frase | Material |
|---|---|---|---|---|
| 1 | **Tool use sin abstracciones** | Carlos Haro (Santander) | Escribir a mano el ciclo que lee lo que el modelo pide, lo ejecuta y responde, y medir cuánto falla. | Repo `h1sort/claude4aieng` · slides en h1sort.com |
| 2 | **Context engineering** | Alejandro Martínez (Platzi) | El contexto es finito: se degrada, y hay formas de resumirlo sin perderlo todo (con el disco como memoria). | Repo `alexMtzRivero/context-engineering-workshop` |
| 3 | **Datos abiertos over MCP** | Dante Bazaldua (Spot2) | Un servidor MCP con datos reales, diseñado para que el modelo elija bien y con controles en el código. | Repo `danteese/claude-mcp-ibero-2026` · PDF de la sesión |
| 4 | **Physical AI + MCP + Swarm Protocol** | Jonathan Olvera (Hiveflow) | Claude con hardware real (una cámara) y agentes que se comunican entre sí, con humano en el loop. | Repo `hiveflowai/physical-ai-workshop` |
| 5 | **Del agente al equipo** | Jésica Tapia (UNESCO) | Auditar un sistema multiagente: barandillas, sesgo, bitácoras y regulación. | Repo de evaluación multiagente (por conseguir) |

Cada carpeta `workshops/NN-*/` trae `notas.md`, `preguntas.md` (tres preguntas por ponente, sobre su experiencia) y `tareas.md`.

## Las ideas que más importan

1. **Una tool es una función que el modelo pide y tu código ejecuta.** El modelo nunca ejecuta nada. *(W1, W3)*
2. **El arnés es ese ciclo.** Un framework solo lo esconde; entender el ciclo te hace mejor ingeniero. *(W1)*
3. **Un error de tool call no siempre es culpa del modelo.** El mismo modelo falla distinto según el proveedor; mídelo por categoría. *(W1)*
4. **El contexto es finito y se degrada** (*context rot*) mucho antes de la ventana anunciada, desde unos ~128 mil tokens según el benchmark que citaron. *(W2)*
5. **Al compactar, guarda el original y deja un puntero.** El resumen pierde detalles; el disco permite recuperarlos sin recargar todo. *(W2)*
6. **MCP da acceso y alcance, y lo pagas en contexto y riesgo.** Para un script fijo basta una API; para tu terminal, una CLI. *(W3)*
7. **Diseña las tools para el agente:** una por intención, respuestas cortas y errores que enseñan a corregirse. *(W3)*
8. **Los controles van en el código, no en el prompt:** validación, idempotencia, aprobación humana. Si la acción es física, más aún. *(W3, W4)*
9. **Entre agentes hace falta identidad y trazabilidad:** quién es cada agente, a quién pedirle cuentas y cómo compartir lo aprendido sin compartir datos. *(W4)*
10. **Las barandillas y las bitácoras con hash importan:** el sistema no decide por la persona, y se puede demostrar qué hizo. *(W5)*
11. **Los sistemas multiagente no son para todo:** son más caros y pueden propagar errores en cascada. *(W2, W5)*
12. **Medir cuesta, pero cambia la confianza.** Evaluar si el modelo elige bien, si sesga y cuánto gasta es parte del trabajo. *(W1, W3, W5)*

## Ruta de estudio (si estás aprendiendo)

1. **Tool y arnés** (conceptos 1–4): lee las notas del W1 y repite el ejercicio del paso 1.
2. **Contexto** (5–9): W2; prueba la compactación con y sin referencia.
3. **MCP y diseño de tools** (10–17): W3; levanta el servidor y pregúntale por el Metro.
4. **Controles y seguridad** (13, 14, 19, 21): junta lo de W3, W4 y W5.
5. **Mundo físico y enjambres** (18–20): W4.
6. **Auditar** (21–23): W5; repite el ejercicio de pares de CVs.

## Lo que se hizo con el código

| Workshop | Estado |
|---|---|
| 1 | Paso 1 (ejecutar las llamadas y devolver los `tool_result`) escrito y comparado con la solución oficial. Las pruebas del repo pasan (110 pasan, 17 se saltan). |
| 2 | Paso 2 (`list_files`, `read_file`, `search_file`, `write_file`) escrito. Pasos 3 a 5 pendientes; la solución del 3 se leyó en la rama `solucion`. |
| 3 | Pasos 2, 3 y 4 copiados y comprobados con `verificar.py` (8 tools, un resource, un prompt). Falta conectar `cdmx` en Claude Code y probar las preguntas. No se corrió `evaluar.py`. |
| 4 | Repo clonado y revisado; **no** se ejecutó ni se flasheó nada. Falta la cuenta de Hiveflow y su API key (las crea la persona). |
| 5 | El repo de la ponente aún no se ha clonado (falta el enlace). |

## Recursos

- Repositorios: [claude4aieng](https://github.com/h1sort/claude4aieng) · [context-engineering-workshop](https://github.com/alexMtzRivero/context-engineering-workshop) · [claude-mcp-ibero-2026](https://github.com/danteese/claude-mcp-ibero-2026) · [physical-ai-workshop](https://github.com/hiveflowai/physical-ai-workshop)
- PDF del W3: `https://stdout.mx/claude4aieng/datos-mcp-ibero.pdf`
- Para profundizar en tool use: el curso 11-768 AI Agents de Carnegie Mellon, **clase 2** (`cmu-agents.com`), que el ponente del W1 recomendó.
- SwarmMind, el tablero de agentes del W4: `swarmind.sh`. Aviso: su `skill.md` hace que un agente se registre solo; revísalo antes de dárselo a uno.
- MCP recomendados en las charlas: Context7 y Parallel (documentación y búsqueda), Blender, Figma.
- El evento: `club.rich`.

## Pendientes y dudas

- **Hueco en el audio:** no se grabó entre las 18:04 y las 18:08 (W1), justo cuando se explicaba la solución del ejercicio.
- **Audio de cierre** (`2048`): no se ha transcrito (networking y foto grupal).
- **Cifras por confirmar:** tasas de error del W1 (modelo y unidades), la fuente del benchmark de degradación del W2, los 3,000 agentes y las cifras del video del W4, y cómo se presenta la ponente del W5.
- **Por hacer:** conseguir el repo del W5, conectar `cdmx` y probar el W3, y crear la cuenta de Hiveflow si se quiere probar el W4.
- **Higiene del repo:** borrar `transcripts/prueba/` y decidir qué commitear (las transcripciones tienen voces de asistentes; las grabaciones no se versionan).

## Cómo se armó esta guía

Cada sesión se grabó con Audio Hijack, se transcribió con la API de Voxtral de Mistral (`tools/transcribe.py`) y se procesó en notas, preguntas y tareas siguiendo `CLAUDE.md`. Los nombres propios y las cifras pueden estar mal transcritos, y por eso las notas los marcan con **(?)**.
