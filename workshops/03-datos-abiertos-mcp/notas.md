# Notas · Datos abiertos over MCP

**Ponente:** Dante Bazaldua (cofundador y CTO de Spot2.mx) · **Fuente:** `transcripts/03-datos-abiertos-mcp/sesion.md` (grabación `20261019 1843`, 39 min, 18:43–19:22).
**Material:** PDF `https://stdout.mx/claude4aieng/datos-mcp-ibero.pdf` (38 págs.) y repo `https://github.com/danteese/claude-mcp-ibero-2026` (clonado en `workshops/03-datos-abiertos-mcp/claude-mcp-ibero-2026`).

> Convención: `[hh:mm:ss]` = marca de la transcripción. **(?)** = dudoso por la transcripción automática (nombres, cifras, términos técnicos). Las diapositivas del PDF sirvieron para contrastar términos mal transcritos, pero los hechos aquí citados con marca son lo que se dijo en el audio.

## Temas en el orden en que se dieron

### 1. Anuncio previo `[00:00:07–00:01:12]`
Se anuncia un concurso o hackathon (en el audio suena "catrón" (?)) ligado a Santander y a México Tech Week: abierto a estudiantes, trabajadores, ingenieros o técnicos; el premio es "ligeramente un secreto" y los jueces serán ejecutivos del banco. Registro abierto. Los detalles son dudosos por la transcripción.

### 2. Arranque y motivación `[00:01:18–00:04:51]`
- Idea: construir un pequeño **servidor MCP** y, desde **Claude Code**, preguntarle cosas `[00:01:36]`; los requisitos son el IDE y las herramientas ya instaladas `[00:01:44]`.
- Pregunta de apertura: cuánta gente pasa en cierta estación del Metro en cierto momento, o cuánto presupuesto tiene tu alcaldía `[00:02:16–00:02:28]`. Dato dado: **más de 4 millones de personas, 149 mil al día, en Pantitlán** `[00:02:49]`.
- **Sin herramientas**, Claude responderá "no puedo darte esa cifra"; **con un MCP** puede responder con el dato `[00:03:30–00:03:57]`.
- El MCP vivirá en tu computadora y se conectará por **HTTP** `[00:03:57–00:04:06]`.
- Preguntas que se resolverán: qué es una tool y qué agrega MCP; diferencia entre MCP, CLI y API; cómo diseñar tools que el modelo use bien; dónde van los controles de una tool que escribe; cómo saber si Claude elige bien `[00:04:14–00:04:46]`.

### 3. Quién es el ponente y Spot2 `[00:04:51–00:07:39]`
Egresado de la Ibero (Ingeniería en Tecnologías de Cómputo y Telecomunicaciones y maestría); trabajó en CERN y UCSD; profesor de asignatura `[00:04:51–00:05:11]`. Cofundador y CTO de **Spot2**, una startup de **bienes raíces comerciales** que busca espacios (bodegas, oficinas, locales) para empresas `[00:05:16–00:05:33]`. En Spot2 tratan a los agentes como **ciudadanos de primera clase**: reciben herramientas para navegar el sitio, pedir citas con propietarios y buscar información `[00:06:34–00:06:56]`; la mayoría de los sistemas está interconectada por MCP `[00:06:58]`.

### 4. ¿Por qué MCP si ya hay REST? `[00:07:39–00:08:13]`
Tiene sentido cuando hay distintos agentes que pueden usar el protocolo; dice que lo desarrolló Anthropic hacia 2024 y que evolucionó a estándar (?) `[00:07:48–00:08:03]`.

### 5. Conceptos `[00:08:50–00:10:17]`
- **Tool:** función que el modelo pide y tu código ejecuta; debe ser lo bastante descriptiva para que el modelo sepa cuándo usarla; el código la ejecuta y regresa un **JSON** `[00:08:52–00:09:24]`.
- **MCP:** estándar para conectar apps de IA (chat, IDEs) con datos (data warehouses, Postgres), herramientas de desarrollo y productividad (Slack); "darle brazos a tu agente" `[00:09:33–00:10:12]`.

### 6. API vs CLI vs MCP `[00:10:17–00:14:03]`
- **API** (GraphQL, REST, SOAP): sirve para un script o pipeline donde el modelo no decide qué traer `[00:10:30–00:10:48]`.
- **CLI:** trabajas en tu terminal y le das comandos al agente, incluso en modo *Auto Accept Permissions* `[00:10:54–00:11:06]`.
- **MCP:** autenticado, se pueden cambiar permisos por el protocolo y controlar quién accede a qué `[00:11:12–00:11:30]`.
- **Lo que da:** funciona sin tu terminal; se instala en Claude.ai o ChatGPT y se conecta a un MCP remoto `[00:11:36–00:11:50]`; **autorización por usuario con OAuth** (ejemplo: Sentry, donde unos usan agentes para corregir errores y otros para reproducirlos) `[00:12:09–00:12:48]`; se escribe una vez y todos lo aceptan `[00:13:10]`.
- **Lo que cuesta:** las definiciones ocupan **contexto y tokens** (el host recibe un "texto gigante" con todas las tools) `[00:11:54–00:13:05]`; **composición:** cada paso pasa por el modelo, y conviene escribir código que llame a tus tools `[00:13:15–00:13:33]`; **seguridad** sin resolver del todo: *tool poisoning* e *injection* en las respuestas `[00:13:33]`; **operación:** otro servicio que desplegar, versionar y probar con cada cliente `[00:13:50]`.

### 7. Host, client, server y capas `[00:14:03–00:16:21]`
- Tres partes: **host, cliente y servidor**. Claude pide la lista de tools y las llama si hace falta; el servidor del repo es de "CDMX" en **Python con FastMCP**, y expone **tools, resources y prompts** `[00:14:03–00:14:32]`.
- Capas obligatorias: mensajes (estándar tipo JSON-RPC), versionado y patrones; el servidor ofrece tools, resources y prompts; el cliente ofrece **elicitation** (cuando Claude te pregunta un dato que le falta) `[00:14:45–00:15:23]`. Menciona aplicaciones de UI completas en el chat (MCP Apps) `[00:15:27]`.
- **Tools** = funciones que invoca el modelo; **resources** = datos de la app (archivos, bases de datos); **prompts** = plantillas `[00:15:47–00:16:12]`.
- **Transporte:** HTTP local (el de hoy), stdio (corre en tu máquina) y remoto (desplegado en un servidor) `[00:16:26–00:16:55]`. Usa FastMCP "por lo fácil que es" `[00:16:55]`.

### 8. Preparación del repo `[00:17:08–00:19:30]`
1. Clonar el repo; hacer `uv sync` para tener los paquetes `[00:17:25]`.
2. `uv run preparar.py`: trae/limpia la afluencia mensual y genera los datos `[00:17:32–00:17:41]`.
3. `uv run verificar.py`: revisa Claude Code, la red y el acceso a los datos `[00:17:52–00:18:09]`.
4. Pregunta «guíame paso a paso» dentro del repo y Claude explica qué hace cada cosa `[00:18:12]`.
5. La rama principal trae **cuatro servidores** que van creciendo en herramientas, para copiar y pegar `[00:18:26–00:18:47]`.
6. **Dos terminales**: una con los logs del servidor y otra con Claude `[00:19:14–00:19:25]`.

### 9. Paso 1: una tool `[00:19:30–00:22:35]`
- El archivo `.mcp.json` le dice a Claude que hay un MCP que usar; Claude pregunta varias cosas antes de iniciar y se acepta `[00:19:32–00:19:54]`.
- Pregunta: «¿Qué datos abiertos hay sobre bicicletas?» → llama `buscar_datasets_cdmx` y responde "hay 11 conjuntos de datos y estos son los primeros 10" (viajes de Ecobici, ubicación de estaciones, infraestructura…) `[00:20:03–00:20:45]`.
- El código: un **decorador** de FastMCP sobre la función; los *hints* del protocolo le dicen a Claude si necesita pedir permiso: si la tool escribe en registros de clientes, interesa que pregunte; si no, puede ejecutarla directa `[00:21:27–00:22:35]`.
- El **docstring** es la descripción que lee el modelo `[00:22:45]`.

### 10. Paso 2: diseño de tools `[00:22:52–00:24:59]`
- "Un API es un contrato, ¿quién lo lee? Los modelos" `[00:22:52]`.
- **No** exponer algo como "ejecutar SQL": es muy amplio y el modelo intentará muchas cosas `[00:23:06]`. Mejor una tool por intención, como `afluencia_metro(estación, línea, desde, hasta)` `[00:23:22–00:23:26]`.
- **Errores que corrigen:** si se escribe "insurgente" y coincide con varias estaciones, el error da feedback para que Claude se autocorrija `[00:23:29–00:23:41]`.
- **Alcance:** que el contexto no explote; devolver lo pedido sin detalles internos de la ejecución `[00:23:48–00:24:11]`.
- Se comprueba con `uv run verificar.py 2`, que genera otro dataset interno `[00:24:11]`; se copia `pasos/02_consulta.py` a `servidor.py`; **hay que reiniciar el servidor cada vez** para que se vean los cambios `[00:24:20–00:24:59]`.
- MCPs que recomienda para investigar: **Context7** y **Parallel**, para que el agente no se detenga por falta de contexto `[00:25:22–00:25:56]`.
- En los logs se ve que cada llamada es un `POST` con respuesta `200` `[00:26:19–00:26:39]`. El paso 4 es el más completo `[00:26:47]`.

### 11. Paso 3: controles en el código `[00:27:02–00:28:53]`
- Para una tool dañina (p. ej. un `INSERT` directo), los controles van en el código y son **deterministas**, no del modelo: **esquemas tipados y cerrados**, **validación**, **idempotencia** (que no se pueda llamar N veces al mismo tiempo) y **aprobación del usuario** con `requiresUserInteraction` `[00:27:10–00:28:30]`.
- La tool de "levantar un reporte" escribe en una base SQLite local, que se ve en el paso 4 `[00:28:30–00:28:53]`.

### 12. Skills y plugins `[00:28:53–00:29:36]`
Además de lo que trae el protocolo, se pueden definir **skills** que enseñan al agente a usar la herramienta mejor; hay **plugins** que combinan MCP y skill, buen patrón para distribuir `[00:28:59–00:29:28]`.

### 13. Evaluaciones `[00:30:03–00:30:57]`
Son "súper importantes": muestran qué tools entiende de verdad el modelo y cuáles necesitan mejor descripción o parámetros más acotados (p. ej., que no haya datos de 2050) `[00:30:03–00:30:36]`. Hay un caso negativo en el script: «¿cuál es la capital de Francia?» no debe usar la tool `[00:30:46–00:30:50]`. Es un pequeño script con casos y argumentos esperados `[00:30:53]`.

### 14. Paso 4: el mapa `[00:31:00–00:34:47]`
El último servidor agrega información a un **mapa de la CDMX** (`mapa/index.html`): se actualiza la información de Ecobici cerca del Metro Insurgentes `[00:31:44–00:32:03]`; se da tiempo para que cada quien lo haga con Claude y el último servidor `[00:32:11–00:32:25]`; el README muestra cómo cambió la afluencia en el tiempo `[00:32:44]`.

### 15. Recap y ideas `[00:34:47–00:36:36]`
- Se construyó un MCP con **8 tools, un resource y un prompt**; se conectó a Claude Code con `.mcp.json` (si no, `/mcp` → *add new* → URL) `[00:35:10–00:35:17]`; evaluación de **10 preguntas**; y el mapa `[00:35:26–00:35:35]`.
- Para llevarse: usar estos datos para otras consultas (**calidad del aire**, las llamadas al **0311**) y crear tools y otra vista `[00:35:39–00:36:01]`.
- MCPs recomendados: **Blender**, **impresoras 3D**, **Figma**, y a diario **Context7** y **Parallel** `[00:36:07–00:36:36]`.

### 16. Buenas prácticas y cierre `[00:36:40–00:38:41]`
- Se diseña para un **usuario que es el agente**, no para personas `[00:36:40–00:37:00]`; no endpoints sueltos para probar `[00:37:00]`.
- **Argumentos planos** `[00:37:10]`; **respuestas cortas** en JSON `[00:37:28]`; **errores que enseñan**, con un artículo citado sobre cómo una empresa ("Perso" (?)) rehízo sus tools para que el agente se autocorrija `[00:37:28–00:37:49]`.
- Criterios **TDQS** (propósito, cuándo usarla, comportamiento, parámetros, concisión y completitud) `[00:37:53]`.
- Es un trabajo **iterativo**: en Spot2 refinan constantemente sus MCP, tools, APIs y CLI `[00:38:03–00:38:16]`. Si falla, se corrige la instrucción `[00:38:33]`.

## Código y comandos mencionados
- `uv sync` · `uv run preparar.py` · `uv run verificar.py` · `uv run verificar.py 2` `[00:17:25–00:24:11]`.
- `cp pasos/02_consulta.py servidor.py` (y los de 03 y 04), reiniciando el servidor tras cada copia `[00:24:20–00:24:59]`.
- `.mcp.json` en el repo; sin él, `/mcp` → agregar URL `[00:19:39, 00:35:17]`.
- Servidor HTTP local de FastMCP con las tools del Metro y Ecobici.

## Dudas abiertas
- Qué es exactamente el concurso anunciado al inicio (nombre, fechas, bases) `[00:00:21–00:01:10]`.
- Si el "artículo de Perso" `[00:37:35]` es el de Philipp Schmid que cita el PDF.
- Si Anthropic desarrolló MCP "por ahí del 2024" `[00:08:03]`; el PDF dice que hoy es un estándar neutral bajo la Linux Foundation.
- Si "tool poisoning" e "injection" quedan sin resolver (cómo lo dijo es ambiguo) `[00:13:33]`.
- Si hay una tercera "tool extra" en el paso 3 (la de levantar un reporte) o si ya viene en el servidor `[00:28:30]`.
