# Flujo de homeopatía para `sistema_consulta`, rediseñado con lo del evento

Propuesta para el módulo 2 (homeopatía) de la skill `sistema-consulta` del repo
`4ailabs/sistema_consulta`. Aplica la tesis del evento: **el modelo propone, la
aplicación ejecuta, y eso se mide.** Las decisiones clínicas siguen siendo del doctor.

Estado: **propuesta en marcha**. F1 y la Regla de los Tres ya funcionan en código; ver [`flujo-homeopatia/README.md`](flujo-homeopatia/README.md) para correrlo.

## El problema que resuelve

| Hoy | Por qué falla | Lección del evento |
|---|---|---|
| Tres instrucciones que se contradicen (protocolo, módulo 02 y hook): mental vs físico primero, bloquear vs prescribir sin datos, 2 vs 3 diferenciales | El modelo elige al azar cuál seguir | Especialistas con una sola tarea y reglas claras (W5) |
| No hay repertorio ni materia médica en el repo: el modelo repertoriza de memoria | "Lo que no dice, el LLM lo va a inventar a menos que se lo prohíbas" (W5 `[00:32:05]`) | Datos reales vía MCP (W3) |
| La regla "¿lo dijo este paciente, en esta consulta?" depende de que el modelo se acuerde | Se cumple en el prompt, no en el código | Original inmutable + puntero (W2); controles deterministas (W3) |
| La receta se puede guardar con `execute_sql` libre; `general_notes` "repetida 10+ veces"; `next_appointment` pasa sin control en el script | Un INSERT válido pero semánticamente peligroso | "No expongas 'ejecutar SQL'" (W3 `[00:23:06]`); llamada válida pero peligrosa (W1) |
| Nadie mide si un cambio en la skill mejora o empeora | No hay casos de prueba | Evals con casos, métricas y juez LLM (W3, W5) |

## El flujo

```
Audio Hijack ─► watcher ─► transcripción diarizada (JSON, INMUTABLE)
                                   │
              ┌────────────────────┘
              ▼
 F1  DEPURADOR  (subagente · solo lee la transcripción)
     síntomas con cita literal + marca de tiempo + ✅/⚠️/🚫 + nivel Kent
              │
              ▼
     [código] validar_caso: cada ✅ debe tener una cita que exista tal cual en la transcripción
              │
              ▼
 F2  REPERTORIZADOR  (subagente · solo tools de repertorio)
     el modelo elige rúbricas ─► [código] eliminar(): filtra remedios, Regla de los Tres
              │
              ▼
 F3  ABOGADO DEL DIABLO  (subagente · contexto separado, no ve el razonamiento de F2)
     ataca el candidato con materia médica + tabla anti-sesgo de policrestos ─► semáforo 🟢🟡🔴
              │
              ▼
 F4  EL DOCTOR DECIDE  (humano en el loop)
              │
              ▼
 F5  [código] guardar_receta(): esquema cerrado, idempotente, con confirmación + bitácora con hash
```

### F0 · Captura (ya existe)

Audio Hijack → `scripts/watch_transcribe.cjs` → Voxtral diarizado → `transcripciones-entrantes/`.
Único cambio: tratar ese JSON como **original inmutable**. Nada lo edita; todo lo demás apunta a él (W2).

### F1 · Depurador de síntomas

- **Entrada:** la transcripción de esta consulta y nada más (ni consultas previas ni otros pacientes).
- **Salida:** `caso.json`, con una entrada por síntoma:
  ```json
  {"sintoma": "...", "cita": "texto literal del paciente", "t": "00:12:31",
   "hablante": "paciente", "clase": "repertorizable|informativo|excluir",
   "nivel": 1, "modalidad": "peor 4-8 pm", "motivo_clase": "..."}
  ```
- **Control en código:** `validar_caso` busca cada `cita` en la transcripción (como `search_file` del W2). Si no aparece literal, el síntoma baja a ⚠️ y se avisa. La regla anti-contaminación deja de depender de la memoria del modelo.
- **Por qué un subagente:** la transcripción completa es larga. El resto del flujo trabaja con `caso.json`, un resumen con punteros (W2: de ~130 mil a ~5 mil tokens sin perder el dato).
- **Pacientes de retorno:** en vez de cargar todas las consultas, una tool `preguntar_historial(pregunta)` que contesta desde los expedientes anteriores, como el `ask_client` del W2.

### F2 · Repertorizador

- **Tools (y solo estas):** `buscar_rubrica(texto)`, `remedios_de_rubrica(id)` y `eliminar(rubricas_generales, rubricas_srp, rubricas_particulares)`.
- **Reparto:** el modelo traduce cada síntoma ✅ a una rúbrica, que es donde aporta. **El código** aplica la eliminación: quién sobrevive cada filtro, qué remedio cae por contradicción modal y si se cumple la Regla de los Tres (≥1 de nivel 1-2, ≥1 SRP y ≥1 de nivel 4). Si no se cumple, `eliminar` responde con un **error que enseña** qué nivel falta, y la salida es "pedir más datos" (W3).
- **Diseño de las tools (W3):** una por intención, argumentos planos, respuestas cortas, docstrings claros.

### F3 · Abogado del diablo

- **Entrada:** `caso.json` y el candidato. **No** ve el razonamiento del repertorizador, para que no herede su sesgo (W5: los especialistas no comparten todo el contexto).
- **Tools:** `materia_medica(remedio)` y la tabla anti-sesgo de policrestos del protocolo actual.
- **Tarea:** buscar el síntoma que separa al candidato de sus diferenciales y verificar las confirmaciones físicas obligatorias (Nat Mur, Sepia, Carcinosin…). Devuelve el semáforo 🟢🟡🔴 con su razón.
- **Auditoría (W5 `[00:32:26]`):** el orquestador puede saltarse especialistas. La bitácora registra qué tools se llamaron; si F3 no corrió, el análisis no se marca 🟢.

### F4 · El doctor decide

Se presenta una tabla: candidato y diferenciales, síntomas a favor y en contra (con su cita y marca de tiempo), semáforo y las preguntas para la próxima consulta. Nada se guarda sin que el doctor lo apruebe (W4: humano en el loop cuando la acción tiene consecuencias).

### F5 · Guardar la receta

- **Una tool cerrada**, `guardar_receta(...)`, en un MCP local (FastMCP, como el W3). Su esquema (Pydantic) **no tiene** `general_notes` ni `next_appointment`: no se pueden llenar porque no existen. `instructions` acepta solo horario y forma de toma.
- **Idempotencia:** un hash de paciente + fecha + medicamentos evita duplicar la receta si la tool se llama dos veces (W3).
- **Confirmación:** la tool pide aprobación antes de escribir (W3: `requiresUserInteraction`).
- **Quitar el SQL libre:** el MCP de Supabase solo en modo lectura (`--read-only`) y con las features mínimas. La escritura pasa por `guardar_receta` o por el script existente, ya con `next_appointment` forzado a null.
- **Bitácora con hash** de cada análisis: qué tools se llamaron, con qué entradas y qué salió. Si alguien la modifica, el hash lo detecta (W5).

### F6 · Evals: saber si un cambio mejora o empeora

| Métrica (por regla, como la tasa de error por categoría del W1) | Cómo se mide |
|---|---|
| % de síntomas ✅ con cita verificable | Código (`validar_caso`) |
| % de análisis que nombran remedio sin cumplir la Regla de los Tres | Código |
| % de recetas con un campo prohibido | Código (debe ser 0 por diseño) |
| ¿F3 corrió? | Bitácora |
| Calidad del diferencial | Juez LLM con rúbrica |
| Caso negativo: solo síntomas comunes de la enfermedad → debe salir 🔴 | Código (caso esperado) |
| **Pares por sexo:** mismo caso, solo cambia hombre/mujer; si aparece Sepia solo en la versión mujer, hay sesgo | Código (W5, la prueba de los CVs `[00:48:21]`) |
| Pares por un general: mismo caso cambiando solo la termicidad → el remedio debe cambiar si la modalidad lo contradice | Código |

- **Casos:** de 10 a 20, **anonimizados**, sacados de consultas reales con desenlace conocido (la tabla `outcomes` de Supabase), más los pares sintéticos.
- **Herramienta:** promptfoo, con aserciones en Python para las reglas y `llm-rubric` para el juez. Se corre antes y después de cada cambio a la skill.

## Herramientas encontradas

| Pieza | Opción | Notas |
|---|---|---|
| Repertorio vía MCP | [OOREP MCP Server](https://mcpmarket.com/server/oorep) ([ficha en Glama](https://glama.ai/mcp/servers/y7s6w9kk3p)) | Da acceso a los repertorios de [OOREP](https://www.oorep.com/) (Kent, Boger, Hering…) y a materias médicas. Se instala con `npx -y oorep-mcp`. **Sin verificar:** su licencia, sus tools y si consulta el servidor público de OOREP (el texto de los síntomas saldría de la máquina, aunque sin nombre del paciente). |
| Repertorio local | [kent-repertory-explorer](https://github.com/su4532/kent-repertory-explorer) | Kent expandido en SQLite, árbol JSON y JSON Lines, con texto de página para trazar cada rúbrica. Avisa que no certifica la exactitud del OCR. Encima se pondría un FastMCP propio con las tools de F2. |
| Repertorio local | [oorep-local-repertory](https://github.com/drwjkirkpatrick-web/oorep-local-repertory) | Repertorio offline construido sobre datos de OOREP. |
| Fuente original | [Kent's Repertory (1899) en Internet Archive](https://archive.org/details/kents-repertory_202403) | Dominio público (Public Domain Mark 1.0). |
| Materia médica | [NLM Digital Collections](https://digirepo.nlm.nih.gov/catalog/nlm:nlmuid-101302367-bk), [Hering, *Condensed materia medica* (Wellcome)](https://wellcomecollection.org/works/pz2urj6p) | Textos históricos digitalizados que la NLM y Wellcome marcan como dominio público. No encontré una copia verificada de la materia médica de Boericke. |
| Más datos | [Tema "homeopathy" en GitHub](https://github.com/topics/homeopathy) | Otros proyectos; revisar la licencia de cada uno. |
| MCP propio | FastMCP (Python) | El que se usó en el W3, con decoradores, docstrings e *hints* de permiso. |
| Supabase seguro | [Supabase MCP](https://glama.ai/mcp/servers/@supabase-community/mcp-supabase/blob/48e3ed1504b1c21801084045c37d967981509925/README.md) con `--read-only` y `features=database` | Ejecuta el SQL con un usuario de Postgres de solo lectura. Las fuentes discrepan sobre si el modo afecta a todas las tools; confirmar en la documentación oficial. |
| Subagentes y bloqueos | Subagentes de Claude Code (`.claude/agents/`) con lista de tools; hooks `PreToolUse` que bloquean con código de salida 2 ([permisos del SDK](https://docs.claude.com/en/api/agent-sdk/permissions), [referencia de tools](https://code.claude.com/docs/en/tools-reference)) | Hubo un [bug, ya cerrado](https://claudeissues.com/issue/43772-subagents-with-bypasspermissions-ignore-pretooluse-hooks-unauthorized-commands-w), en que los subagentes con `bypassPermissions` se saltaban los hooks: verificarlo en la versión instalada. |
| Evals | [promptfoo](https://www.datacamp.com/tutorial/promptfoo-tutorial), con una [skill para Claude Code](https://skills.cat/skills/daymade/claude-code-skills/promptfoo-evaluation) | `llm-rubric` como juez; si solo está `ANTHROPIC_API_KEY`, usa Claude para calificar. Guarda las respuestas en caché para no pagar de nuevo. |

## Orden de implementación

Lo más barato y de mayor efecto primero. Los subagentes al final, porque son caros y "no son para todo" (W2 `[00:29:53]`, W5 `[00:19:21]`).

1. **Unificar las tres instrucciones** en un solo flujo. Necesita dos decisiones del doctor (abajo).
2. **F5:** corregir `next_appointment` en el script y quitar `execute_sql` de la skill. Después, `guardar_receta` en FastMCP.
3. **F6:** de 10 a 20 casos anonimizados y los pares, en promptfoo. Correrlos sobre la skill actual para tener una línea base.
4. **F1:** `caso.json` con citas y `validar_caso`.
5. **F2:** repertorio local (Kent en SQLite) y FastMCP con `buscar_rubrica` y `eliminar`.
6. **F3 y subagentes:** solo si las evals muestran que una sola pasada no basta.

## Decisiones del doctor (antes del paso 1)

1. ¿Por dónde se empieza: generales mentales (Kent, como dice el protocolo) o síntomas físicos (como dice el hook)?
2. Si no se cumple la Regla de los Tres, ¿se bloquea (🔴, pedir datos) o se permite 🟡 con potencia baja?
3. ¿Repertorio local (los datos no salen de la Mac) u OOREP en línea?
