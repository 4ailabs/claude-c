# Conceptos del evento, en orden

Mapa de lo visto en los workshops, ordenado de lo más básico a lo más avanzado. Cada concepto dice **qué es**, **qué dijo cada ponente** y **qué recordar**.

- **Cubierto:** los cinco workshops: 1 (Carlos Haro), 2 (Alejandro Martínez), 3 (Dante Bazaldua), 4 (Jonathan Olvera) y 5 (Jésica Tapia).
- **Fuentes:** `W1` a `W5` = la transcripción de cada workshop, con su marca `[hh:mm:ss]`. `W1·P2` y `W1·P3` son las partes 2 y 3 del workshop 1. Detalle y dudas en `workshops/NN-*/notas.md`. `(?)` = dudoso por la transcripción automática.
- Alimenta la guía final (`docs/guia-final.md`, el cierre según `docs/flujo.md`).

## Hilo conductor

> **El modelo propone, la aplicación ejecuta, y eso se mide.**

De ahí salen cinco bloques: *cómo actúa un agente* (conceptos 1–4), *qué contexto ve* (5–9), *cómo se conecta con el mundo de forma segura* (10–17), *qué pasa cuando actúa en el mundo físico y con otros agentes* (18–20) y *cómo se audita y se responde por él* (21–23).

## Mapa rápido

| # | Concepto | Workshop |
|---|---|---|
| 1 | Un modelo solo predice tokens | W1, W3 |
| 2 | Tool: el modelo pide, tu código ejecuta | W1, W3 |
| 3 | El arnés (harness) | W1 |
| 4 | Por qué fallan los tool calls y cómo medirlo | W1 |
| 5 | Contexto y *context rot* | W2 |
| 6 | Compactación, sin y con referencia | W2 |
| 7 | El disco como memoria | W2 |
| 8 | Otras técnicas de contexto | W2 |
| 9 | Subagentes como contexto | W2 |
| 10 | MCP: qué es y sus piezas | W3 |
| 11 | MCP, CLI o API | W3 |
| 12 | Diseñar tools para un agente | W3, W1 |
| 13 | Controles cuando una tool escribe | W3, W1 |
| 14 | Seguridad: *tool poisoning* e *injection* | W3 |
| 15 | Skills y plugins | W3 |
| 16 | Evaluar si el modelo elige bien | W1, W3 |
| 17 | Criterio de ingeniería: cuándo sí y cuándo no | W2, W3 |
| 18 | *Physical AI*: del agente al mundo físico | W4 |
| 19 | Humano en el loop y consecuencias físicas | W4, W3 |
| 20 | Enjambres: agentes que hablan con agentes | W4 |
| 21 | Barandillas (*guardrails*) | W5, W4 |
| 22 | Auditar sesgo y evaluar un sistema | W5 |
| 23 | Regulación, bitácoras y privacidad | W5, W4 |

---

## Bloque A · Cómo actúa un agente

### 1. Un modelo solo predice tokens
- **Qué es:** el modelo recibe tokens y predice tokens; por sí solo **no sabe** lo que pasó después de su entrenamiento ni **puede hacer** cosas.
- **W1:** "un modelo de lenguaje tiene tokens… lo único que es son tokens" `[00:43:15–00:43:19]`. Los tokens especiales de un modelo **abierto** (como Qwen) se conocen; los de un modelo **privado** no, porque se introducen en el aprendizaje por refuerzo posterior al preentrenamiento `[00:44:00–00:44:26]`.
- **W3:** el modelo "solamente recibe tokens y predice tokens; le falta saber y poder hacer cosas" `[00:05:40–00:05:50]`.
- **Recordar:** lo único que sí se ve de un modelo cerrado es el JSON de la API.

### 2. Tool: el modelo pide, tu código ejecuta
- **Qué es:** una función con nombre, descripción y parámetros que el modelo puede **pedir** que se ejecute.
- **W1:** la API devuelve `stop_reason: tool_use` con un bloque que trae `id`, `name` e `input`; tu código ejecuta y responde con un `tool_result` con ese `id` `[00:45:06–00:45:47]`. "La aplicación sigue siendo el mayor", es decir, la que manda `[00:48:50]`.
- **W3:** "una tool es una función que el modelo pide y tu código ejecuta"; debe ser lo bastante descriptiva para que el modelo sepa **cuándo** usarla `[00:08:52–00:09:24]`.
- **Recordar:** el modelo nunca ejecuta nada, solo pide.

### 3. El arnés (harness)
- **Qué es:** el código que lee lo que el modelo pidió, lo ejecuta y le devuelve el resultado, en bucle.
- **W1:** los frameworks (LangChain (?), Pydantic AI (?), Microsoft Agent Framework) hacen lo mismo: parsean ese JSON y ejecutan las tools `[00:47:43–00:48:17]`. La lección final: sea con un framework, con el SDK o con otra librería, **el arnés usa primitivas de este estilo**; entender los internos "nos hace mejores ingenieros" `W1·P3 [00:00:48–00:01:19]`.
- **Ejercicio del taller:** el paso 1 (ejecutar las llamadas y devolver **un** mensaje de usuario con un `tool_result` por llamada) `W1·P3 [00:00:15–00:00:48]`.

### 4. Por qué fallan los tool calls y cómo medirlo
- **W1:** en OpenRouter, el mismo modelo tiene **tasas de error de tool call muy distintas según el proveedor** `[00:31:31–00:33:27]` (cifras citadas: 11.1%, 0.15–0.44 y 17.3%, con modelo y unidades dudosos).
- **Hipótesis de la audiencia:** saturación, definición ambigua de la tool, cómo se ofrece el output estructurado, rate limit `[00:33:51–00:34:34]`.
- **Hipótesis del ponente:** cuantización y **decodificación restringida** `[00:35:52–00:36:09]`.
- **Del repo del taller (no del audio):** se rompe el agente a propósito de tres formas: historial con `tool_use` huérfano, JSON truncado por `max_tokens` y una llamada válida pero peligrosa.
- **Recordar:** un error de tool call no siempre es culpa del modelo; hay que medirlo por categoría.

---

## Bloque B · Qué contexto ve el agente

### 5. Contexto y *context rot*
- **Qué es:** contexto = todo lo que se le da al modelo: instrucciones, **tools**, el chat actual, resúmenes y el contexto buscado (búsqueda web, documentos, respuestas de otros agentes) `W2 [00:03:39–00:04:27]`.
- **Context rot:** la ventana de 1 millón de tokens no es plenamente usable; la calidad se degrada desde unos ~128 mil tokens, según un benchmark cuyo nombre no quedó claro `W2 [00:05:05–00:06:21]`.
- **En vivo:** con ~130–200 mil tokens, Haiku contestó "no puedo responder" aunque el dato estaba, y a veces respondió seguro pero mal `W2 [00:11:28–00:12:42]`.
- **Cuándo importa:** agentes de horizonte largo (8–15 horas), conversaciones largas y sistemas multiagente `W2 [00:06:38–00:08:13]`.
- **Conecta con:** las definiciones de tools **también** ocupan contexto (concepto 11).

### 6. Compactación, sin y con referencia
- **Qué es:** reemplazar el historial por un resumen más corto.
- **Sin referencia:** responde lo básico, pero un detalle (p. ej. un número de serie) se pierde `W2 [00:15:34–00:16:11]`; todo algoritmo de compactación pierde información `W2 [00:15:09–00:15:19]`.
- **Con referencia:** se guarda el original en disco (inmutable) y el resumen lleva un **puntero**; "para un LLM, un puntero es texto plano" `W2 [00:19:01–00:19:49]`. El contexto pasó de ~130,000 a ~5,000 tokens (cifra a confirmar) `W2 [00:21:03]`.
- **Idea clave:** "no todo tiene que estar fresco todo el tiempo en la mente del agente" `W2 [00:21:35]`.

### 7. El disco como memoria
- **Qué es:** darle al agente herramientas para guardar y buscar en archivos: `write_file`, `search_file` (como `grep`) y `read_file` (un rango de líneas) `W2 [00:16:17–00:17:49]`.
- **Por qué:** lo que devuelve una tool entra completo al contexto, así que se busca primero y se lee solo lo necesario.
- **Hecho en este repo:** el paso 2 (`paso2_disco.py`) está escrito.

### 8. Otras técnicas de contexto
- **W2 `[00:21:52–00:24:50]`:** truncar (los 100 mensajes más recientes de 1,000), limpiar resultados de tools, compresión por tokens, notas, subagentes, y resumen total, parcial (la mitad vieja) o estructurado.
- **Opinión del ponente:** el resumen estructurado **no** lo recomienda, porque el siguiente modelo "va a deshacer cualquier implementación a la medida" (idea de la *bitter lesson* (?)); prefiere la compactación con referencia al disco, que "ha sobrevivido varios modelos" `[00:24:20–00:24:50]`.

### 9. Subagentes como contexto
- **Qué es:** en vez de cargar todo en un agente, se instancian varios, cada uno con su parte, y un orquestador les hace preguntas `W2 [00:25:18–00:27:17]`.
- **Efecto:** el contexto estático se vuelve dinámico y, al guardarse en disco, es **auditable** `W2 [00:27:30–00:28:12]`.
- **Contrapeso:** los sistemas multiagente usan más contexto que un solo agente `W2 [00:07:40–00:08:13]`; "el negocio es orquestar un equipo de subagentes", no solo crear agentes `W1 [00:20:12]`.
- **W5:** el orquestador **no comparte toda la conversación** con los demás agentes por diseño; si el contexto se compacta mal se pueden perder las barandillas, y un error al pasar el contexto produce **errores en cascada** que nadie nota `[00:19:37–00:20:43]`. Cada especialista puede usar un modelo distinto: "no necesitas toda la potencia para todo" `[00:19:00–00:19:16]`.

---

## Bloque C · Conectar el agente con el mundo

### 10. MCP: qué es y sus piezas
- **Qué es:** un estándar abierto para conectar apps de IA con datos y herramientas externas `W3 [00:09:33–00:10:12]`.
- **Tres actores:** host (Claude Code), cliente (el conector) y servidor (tu código, aquí en Python con FastMCP) `W3 [00:14:03–00:14:39]`.
- **Qué ofrece un servidor:** *tools* (decide el modelo), *resources* (datos de la app) y *prompts* (plantillas) `W3 [00:15:47–00:16:12]`; el cliente puede ofrecer *elicitation* `[00:15:10]`.
- **Transportes:** HTTP local (el de hoy), stdio y remoto `W3 [00:16:26–00:16:55]`.

### 11. MCP, CLI o API
- **API:** sirve para un script o pipeline donde el modelo no decide qué traer. **CLI:** trabajas en tu terminal con herramientas que el modelo ya conoce. **MCP:** autenticado, con permisos y control de quién accede a qué `W3 [00:10:17–00:11:30]`.
- **Lo que da MCP:** funciona sin tu terminal (Claude.ai, ChatGPT), autorización por usuario con OAuth y se escribe una vez `W3 [00:11:36–00:13:10]`.
- **Lo que cuesta:** tokens por las definiciones, cada paso pasa por el modelo, seguridad abierta y otro servicio que operar `W3 [00:11:54–00:14:03]`.

### 12. Diseñar tools para un agente
- **W3:** una tool es un **contrato que lee el modelo** `[00:22:52]`. No exponer "ejecutar SQL" (muy amplio); una tool **por intención**, como `afluencia_metro(estación, línea, desde, hasta)` `[00:23:06–00:23:26]`. Errores que **corrigen** (si "insurgente" coincide con varias estaciones, el error ofrece las opciones) `[00:23:29–00:23:41]`. **Respuestas cortas**, argumentos planos y errores que enseñan `[00:37:10–00:37:49]`. Criterios TDQS: propósito, cuándo usarla, comportamiento, parámetros, concisión y completitud `[00:37:53]`.
- **W1:** una de las causas propuestas del error de tool call es que "la definición del tool es ambigua" `[00:34:03]`.

### 13. Controles cuando una tool escribe
- **W3:** los controles van en el **código** y son **deterministas**, no del modelo: esquemas tipados y cerrados, validación, **idempotencia** y aprobación del usuario con `requiresUserInteraction` `[00:27:02–00:28:30]`. Los *hints* del protocolo (p. ej. solo lectura) le dicen a Claude si debe pedir permiso `[00:22:08–00:22:35]`.
- **W1 (repo):** una llamada válida pero peligrosa se detiene con una compuerta en el paso 4.
- **Recordar:** nunca solo en el prompt.

### 14. Seguridad: *tool poisoning* e *injection*
- **W3:** son temas de seguridad "que todavía no se resuelven": el resultado de una tool puede traer texto que el modelo trate como instrucciones `[00:13:33–00:13:42]` (la formulación exacta es ambigua).
- **W5:** también el contenido que aporta una persona es entrada no confiable: un candidato puede esconder **una instrucción para el LLM dentro de su CV** `[00:36:01–00:36:56]` (concepto 22).
- **Conecta con:** el texto que vuelve de una tool es **entrada no confiable** (concepto 13).

### 15. Skills y plugins
- **W3:** una skill enseña al agente a usar bien una herramienta; un plugin combina el MCP y la skill, y es un buen patrón para distribuir `[00:28:53–00:29:36]`.

### 16. Evaluar si el modelo elige bien
- **W3:** las evaluaciones muestran qué tools entiende el modelo y cuáles necesitan mejor descripción o parámetros más acotados; incluyen casos negativos (p. ej. «¿cuál es la capital de Francia?» no debe usar la tool) `[00:30:03–00:30:57]`. Si falla, se corrige la instrucción de la tool `[00:38:33]`.
- **W1:** el taller termina midiendo la tasa de error de herramientas de tu propio agente, por categoría y con costo.

### 17. Criterio de ingeniería: cuándo sí y cuándo no
- **W2:** implementar estos mecanismos en producción no siempre conviene: puede romperse la **caché**, subir el costo o agregar una capa que no da mucho beneficio; "hay que saber cuándo compactar" y el umbral depende del sistema `[00:29:53–00:30:59]`.
- **W3:** es un trabajo iterativo: en Spot2 refinan constantemente sus MCP, tools, APIs y CLI `[00:38:03–00:38:16]`.
- **W5:** "los sistemas de agentes **no son para todo**": son más verbosos y caros, y **evaluar también cuesta** `[00:19:21–00:19:37]` · `[00:39:28–00:40:31]`.

---

## Bloque D · Del agente al mundo físico y al enjambre

### 18. *Physical AI*: del agente al mundo físico
- **Qué es:** que Claude opere en el mundo real, no solo en el digital, conectado a hardware (aquí, una placa ESP32 con cámara).
- **W4:** "una placa **ve, pero no piensa**" `[00:11:00]`: la placa toma la foto (al cambiar la escena) y **Claude la describe** en la nube; hay modelos pequeños que correrían en la placa, "pero no son tan inteligentes" `[00:10:19–00:10:28]`. Los sensores por sí solos solo detectan encendido/apagado o un valor `[00:11:19]`.
- **Idea para casa:** conectar la placa a la computadora y pedirle a Claude cómo leer los sensores; se pueden construir **MCP alrededor de la placa** `[00:15:01–00:16:46]`.
- **Recordar:** misma arquitectura que antes (el agente propone, otro ejecuta), pero ahora el "ejecutar" toca el mundo.

### 19. Humano en el loop y consecuencias físicas
- **W4:** "¿qué pasa cuando se trata de una **válvula**?": el código que falla suele arreglarse, lo físico no `[00:08:43–00:09:21]`. "La responsabilidad cae en ti como ingeniero" `[00:09:40]`.
- **Controles que propone:** definir las consecuencias físicas y los valores "rojos", y la **frecuencia** de revisión según el riesgo (fuego cada segundo, una fuga de agua cada minuto), **bitácora** y un **humano que confirme** `[00:17:25–00:18:23]`. En su simulación, el enjambre pide permiso a un humano cuando **dos o tres criterios** apuntan a una emergencia `[00:20:46–00:21:33]`. Cierre: el modelo puede equivocarse, así que el humano aprueba o rechaza desde el celular `[00:34:20–00:35:13]`.
- **Conecta con:** el concepto 13 (los controles van en el código y son deterministas) y la idea de *tool* peligrosa del W3.

### 20. Enjambres: agentes que hablan con agentes
- **W4:** "la siguiente ola" es que **los agentes interactúen con los agentes de otras personas**, lo que exige protocolos de **seguridad y comunicación** `[00:04:37–00:05:43]`.
- **Video de cierre (W4, en la grabación del W5):** simulación de hospitales donde el que detecta una estafa comparte **solo el patrón** (la "vacuna", aprobada por una persona) y los impostores sin **identidad firmada** se rechazan en la puerta `W5 [00:00:19–00:03:50]`.
- **Caso real:** un proyecto público (un tablero Kanban para agentes, SwarmMind (?)) recibió unos **3,000 agentes** en la primera semana `[00:19:45–00:20:04]`. Para poder responsabilizar a un agente, **un correo por agente** con el que ver qué hace `[00:20:09–00:20:35]`.
- **Protección compartida:** si un nodo "se infecta", aprende y lo **comparte** con la red, como una vacuna `[00:21:33–00:22:45]`.
- **Riesgo de la caja negra:** buscar lo agéntico **y** lo visual para humanos, de modo que un compañero no técnico pueda ver dónde se atoró un flujo `[00:35:18–00:36:21]`.
- **Conecta con:** el concepto 14 (el texto que viene de otros es entrada no confiable) y el 9 (subagentes).

---

## Bloque E · Cómo se audita y se responde por un sistema

### 21. Barandillas (*guardrails*)
- **Qué es:** reglas que limitan lo que el sistema puede hacer o decir, puestas **a la entrada y a la salida** `W5 [00:18:30–00:18:55]`.
- **W5:** en el caso de selección de CVs, el sistema **nunca recomienda a quién contratar** (eso se reserva a las personas, por el *sesgo de automatización*) y tiene prohibido inventar lo que el CV no dice `[00:29:14–00:30:22]` · `[00:32:05]`. Conviene **definir todos los agentes y barandillas en un solo lugar** para poder encontrarlos `[00:25:57–00:26:38]`.
- **W4 (video):** capas de defensa: un filtro rápido antes del modelo grande y un **mandato firmado**, donde el modelo solo propone y los compromisos necesitan la firma de la persona `W5 [00:01:49–00:02:45]`.
- **Recordar:** una barandilla que se pierde al compactar el contexto ya no protege (conceptos 6 y 9).

### 22. Auditar sesgo y evaluar un sistema
- **W5:** el sesgo **no viene solo de los datos**, también de los hábitos humanos: pedir "mucha disponibilidad" excluye, sin decirlo, a quien tiene otras obligaciones `[00:17:17–00:18:09]`.
- **Cómo se prueba:** comparar una corrida **ingenua** con una **protegida**; usar **pares de CVs idénticos** que solo cambian hombre/mujer; cambiar idiomas; agregar una señal indirecta (universidad pública o privada) `[00:34:20–00:43:10]` · `[00:46:39–00:48:44]`.
- **Qué vigilar:** que no se mencionen atributos protegidos aunque vengan de un modelo predictivo ya sesgado `[00:41:18–00:42:32]`; que el orquestador **sí consulte** a los especialistas (revisar qué herramientas llamó) `[00:32:26–00:33:23]`; y que "lo que no dice, el LLM lo inventa" a menos que se prohíba `[00:32:05]`.
- **Conecta con:** las evaluaciones del concepto 16, pero aquí para **sesgo y cumplimiento**, no solo para ver si el modelo elige bien.

### 23. Regulación, bitácoras y privacidad
- **W5:** el AI Act de la Unión Europea apunta a usos como educación y salud, y exige **bitácoras** `[00:21:40–00:22:02]`. Las bitácoras llevan **hash** para detectar modificaciones: "la tentación de modificarlas cuando algo falla es mucha" `[00:22:06–00:22:31]`.
- **Tensión sin resolver:** hay que guardarlo todo, pero hay datos personales; "no está bien resuelto en las leyes" `[00:37:27–00:38:09]`.
- **W4 (video):** cada decisión queda en una **bitácora encadenada** que un regulador puede verificar `W5 [00:02:20–00:02:30]`.
- **Dashboards:** auditar en producción genera demasiada información; hacen falta vistas distintas para cada público (legal, no técnicos) `[00:25:07–00:25:44]`; y tras la evaluación la gente **confía de otra forma** en el sistema `[00:44:58–00:45:39]`.

---

## Cosas por confirmar

- Cifras de OpenRouter del W1 (modelo y unidades), y la fuente del benchmark de degradación del W2.
- Si la reducción de contexto del W2 fue de ~130 mil a ~5 mil tokens.
- Qué dijo el W1 entre las 18:04 y las 18:08 (no se grabó).
- Formulación exacta de "tool poisoning / injection" del W3.
- Nombres citados con duda: skill de compresión (W2), artículo sobre errores que enseñan (W3), concurso anunciado al inicio (W3), nombre de la empresa y proyectos del W4 (Hiveflow, "FarmMind/FarmOut" ≈ SwarmMind), cifra de ~3,000 agentes y reglas del regalo de la placa (W4), cifras del video (16 y 12 ataques) y cómo se presenta la ponente del W5 (empresa e institución).

## Fuentes

- Notas completas de cada workshop: `workshops/NN-*/notas.md`. Transcripciones: `transcripts/NN-*/sesion.md`.
