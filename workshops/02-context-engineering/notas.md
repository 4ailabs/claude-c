# Notas · Context engineering

**Ponente:** Alejandro Martínez (Senior Software Engineer, Platzi) · **Fuente:** `transcripts/02-context-engineering/sesion.md` (grabación `20261019 1811`, 31.8 min, 18:11–18:43).
**Repo:** `github.com/alexMtzRivero/context-engineering-workshop` (clonado en `workshops/02-context-engineering/context-engineering-workshop`).

> Convención: `[hh:mm:ss]` = marca de la transcripción. **(?)** = dudoso por la transcripción automática (nombres, cifras, términos técnicos). Nada está corregido de memoria.

## Temas en el orden en que se dieron

### 1. Arranque y presentación `[00:00:02–00:02:40]`
- Preguntas a la sala: quién es estudiante o trabaja (50-50), quién usa Claude u OpenAI `[00:00:30–00:00:55]`. Pregunta si el editor de código se seguirá usando `[00:00:58]`.
- Se presenta: Senior Software Engineer en Platzi `[00:01:28]`. Tema: **context engineering**, en concreto **mecanismos de compactación y cómo usar el disco** para mejorarlos `[00:01:33–00:01:40]`.
- Por tiempo **no cubre "tools bajo demanda"** (paso 4); todo se hace con el framework "Pylantic" (?) = Pydantic AI `[00:01:45]`.
- Afirma que lleva "un año, año y medio" sin editar una línea de código a mano: "toca leer mucho código" `[00:02:00–00:02:06]`.
- Platzi: más de 7 millones de estudiantes y capacitación a más de 4 mil empresas `[00:02:19–00:02:29]`.

### 2. Repo y arranque `[00:02:40–00:03:39]`
- QR "transitorio" con el repo; si no, buscar su usuario en GitHub (el repo está fijado en el perfil) `[00:02:47–00:03:10]`.
- El README explica instalar `requirements` y correr un pequeño servidor Uvicorn; no lo cubre porque los asistentes deberían poder hacerlo `[00:03:19–00:03:30]`.
- Recomienda **ir a la rama `solucion`**, porque el tiempo no alcanza `[00:08:26]`; los algoritmos implementados son muy simples y se pueden mejorar `[00:08:33–00:08:40]`.

### 3. Qué es el contexto `[00:03:39–00:04:27]`
Todo lo que se le da al modelo para la tarea: prompts de instrucciones, **tools**, el chat actual, **resúmenes** y el **contexto buscado** (búsqueda web, documentos, respuestas de otros agentes).

### 4. Historia y *context rot* `[00:04:27–00:06:26]`
- 2020: unos 2,000 tokens; 2024: Gemini con 2 millones; hoy el estándar vendido es 1 millón `[00:04:29–00:04:50]`.
- **Context rot:** el millón de tokens no es plenamente usable `[00:05:05]`. Cita un benchmark reciente de un modelo (nombre dudoso: "Kibin Eye 3.7 Flash" / "Gemini 3.6" (?)) en el que la calidad se degrada desde ~128 mil tokens `[00:05:13–00:06:10]`; dice que no hay datos tan modernos de Opus, Haiku o Sonnet y que la degradación aparece "incluso a los 120 mil" `[00:06:10–00:06:21]`.
- Cómo miden: datasets sintéticos, ventana llena de conversaciones, y preguntas como "¿cuál fue el segundo mensaje?" `[00:05:27–00:05:46]`.

### 5. Cuándo importa `[00:06:26–00:08:13]`
- **Agentes de horizonte largo** (corren 8–15 horas); los *harnesses* tienen políticas de compresión por detrás `[00:06:38–00:07:00]`.
- **Conversaciones largas**, p. ej. soporte a un cliente con dos años de historial `[00:07:07–00:07:38]`.
- **Sistemas multiagente:** producen más información y usan más contexto que un solo agente (atribuido a un estudio de "antropología" (?) = probablemente Anthropic) `[00:07:40–00:08:13]`.

### 6. Dataset de la práctica `[00:08:46–00:09:53]`
Simula una empresa que vende equipo a call centers: **5 clientes, ~200 mil tokens**. A todos se les vendieron 40 audífonos, llegaron 36 y de esos 2 dañados. Los casos se repiten entre clientes, con números de serie distintos.

### 7. Context rot en vivo `[00:09:53–00:12:50]`
1. Pulsar "cargar conversación muy larga" `[00:10:03]`.
2. Usar **Anthropic Haiku** con la key de Anthropic (los asistentes "tienen" una key) para no gastar tokens `[00:10:11–00:10:28]`.
3. Pregunta rápida: **"¿cuál de los cinco clientes recibe su reposición primero?"** `[00:11:28]`.
4. Haiku responde **"No puedo responder con los datos de esta conversación"** aunque la información está `[00:12:12–00:12:25]`.
5. A veces respondió con seguridad pero con datos incorrectos `[00:12:30–00:12:42]`.
6. Dice que algo que descubrió afectará sistemas de producción de Platzi `[00:10:41–00:10:57]` (la transcripción es confusa en esta parte).
- Cifras citadas: ventana "de 130 mil" que llega a "200 mil" tokens `[00:12:06]` (el README del repo dice ~205 mil).

### 8. Compactación ingenua `[00:12:50–00:16:11]`
- Un agente resume el historial. El prompt dice solo "haz un resumen" `[00:14:35]`; el resumen es "mediocre cuando mucho" `[00:13:53]`.
- Efecto: el contexto de **1.3 MB baja a unos kilobytes** (cifra exacta dudosa) `[00:14:21]`.
- **Compactar sin referencia:** responde lo básico, pero un detalle como un **número de serie** se pierde, porque no sabe qué era importante para ti `[00:15:34–00:16:11]`.
- Todos los algoritmos de compactación pierden información `[00:15:09–00:15:19]`.

### 9. Disco como memoria: compactar **con referencia** `[00:16:17–00:21:35]`
- Dos herramientas de fondo (tres en el repo): **leer y escribir en disco** `[00:16:17]`. `search_file` es "un grep" (expresión regular sobre un archivo) `[00:17:16]`; `read_file` trae, por ejemplo, las líneas 100 a 200 `[00:17:28]`; `write_file` guarda el resumen `[00:17:38]`.
- Flujo de `compact` `[00:19:01–00:19:49]`: guarda el chat completo (el **original queda inmutable**) → llama al agente que resume → si hay referencia, guarda el original en disco y agrega un **puntero**: "el historial completo está en este archivo; si faltan detalles, búscalos". Para un LLM, **un puntero es texto plano** `[00:19:41]`.
- Resultado: ante la misma pregunta de la reposición, el contexto pasó de **~130,000 tokens a ~5,000** y el agente encontró el dato (una fecha, "domingo 18 de octubre") buscando en el archivo `[00:21:03–00:21:35]`.
- Idea clave: "no todo tiene que estar fresco todo el tiempo en la mente del agente" `[00:21:35]`.

### 10. Catálogo de técnicas de *context engineering* `[00:21:52–00:24:50]`
- **Truncar:** de 1,000 mensajes, quedarse con los 100 más recientes `[00:22:09–00:22:21]`.
- **Limpiar resultados de tools:** en producción llenan el contexto `[00:22:23–00:22:37]`.
- **Compresión por tokens:** una skill de "Kate Mann Speech" (?) que hace hablar al agente "como cavernícola" (?) para ahorrar tokens `[00:22:37–00:23:05]`.
- **Notas:** el agente decide qué guardar para después `[00:23:12–00:23:41]`.
- **Subagentes** `[00:23:41]`.
- **Resumen total, parcial (la mitad vieja) y estructurado** `[00:23:48–00:24:20]`. El **estructurado no lo recomienda**: va contra la "peer lesson" (?) = *bitter lesson*, porque el siguiente modelo "va a deshacer cualquier implementación a la medida" `[00:24:20–00:24:34]`.
- Su preferencia: **compactación con referencia al disco**, que "ha sobrevivido varios modelos" en Platzi `[00:24:34–00:24:50]`.

### 11. Subagentes como contexto `[00:25:18–00:29:34]`
- El dataset lo generó otro agente de servicio al cliente: ¿por qué cargarlo entero como contexto estático? `[00:25:40–00:26:10]`.
- Se **instancian cinco agentes**, uno por cliente, cada uno con su conversación pequeña; un **orquestador** (el mismo chat) les hace las preguntas `[00:26:24–00:27:17]`.
- El contexto deja de ser estático y se vuelve **dinámico**: se pueden pedir reportes o estadísticas `[00:27:30–00:27:48]`. Al guardar en disco, **todo es auditable** `[00:27:56–00:28:12]`.
- La tool `ask_client` es "como cualquier otra tool": busca la conversación del cliente, le da al subagente ese contexto y una pregunta, y devuelve la respuesta al contexto general `[00:28:40–00:29:08]`.

### 12. Cierre `[00:29:43–00:31:18]`
- Hay que saber qué pasa detrás de cada mecanismo `[00:29:43–00:29:50]`.
- Implementó varios en producción "no porque sirvan": puede romperse la **caché** y subir los costos, y una capa extra de tools puede no dar mucho beneficio `[00:29:53–00:30:23]`.
- **Hay que saber cuándo compactar**; el umbral depende del sistema (200, 300 o 400 mil tokens) `[00:30:34–00:30:59]`.
- Contacto: redes y LinkedIn `[00:31:08]`.

## Código y comandos mencionados
- Servidor del repo: Uvicorn (ver README del repo) `[00:03:19]`.
- Rama `solucion` del repo `[00:08:26]`.
- Herramientas de disco: `search_file` (≈ grep), `read_file` (rango de líneas), `write_file` `[00:17:16–00:17:38]`.
- `compact` con y sin referencia; `ask_client` para subagentes `[00:19:01, 00:28:40]`.

## Dudas abiertas
- Nombre del modelo y fuente del benchmark de degradación (130 mil / 120 mil tokens) `[00:05:13]`.
- Cifra exacta de la reducción 1.3 MB → "kilobytes" `[00:14:21]` y si 130 mil vs 205 mil tokens es el total real `[00:12:06]`.
- Qué dijo exactamente sobre los sistemas de producción de Platzi afectados `[00:10:41]`.
- Nombre de la skill de compresión ("Kate Mann Speech") y el estudio citado sobre multiagente.
- Si dejó alguna tarea formal: dice que "esto ya se nos dejará de tarea" `[00:21:16]`, pero la frase es dudosa.
