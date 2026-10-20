# Notas · Tool use sin abstracciones

**Ponente:** Carlos Haro (Santander) · **Fuentes (tres grabaciones):**
- `sesion.md`: `20261019 1705`, 52 min (17:05–17:57). Marcas `[hh:mm:ss]` sin prefijo.
- `sesion-parte2.md`: `20261019 1757`, 6.7 min (17:57–18:04). Marcas con prefijo **P2**.
- `sesion-parte3.md`: `20261019 1808`, 3.1 min (18:08–18:11). Marcas con prefijo **P3**.

**Alcance:** todo el workshop, con un **hueco sin grabar entre las 18:04 y las 18:08** (la grabación se cortó). Lo más probable es que ahí estuviera la solución del ejercicio, pero no hay audio que lo confirme.

> Convención: `[hh:mm:ss]` = marca de la transcripción. **(?)** = dudoso por la transcripción automática (nombres, cifras, términos técnicos). Nada aquí está corregido de memoria.

## Contexto previo al workshop (no es del ponente)

- `[00:00:00–00:03:21]` Bienvenida de Rich: 11 eventos del 19 al 30 de octubre (club.rich); pide mandar fotos y videos a Anthropic.
- `[00:03:25–00:11:07]` Alejandro Anaya (Ibero): más de 1,600 solicitudes, 1,300 en lista de espera.
- `[00:12:13–00:21:37]` "State of Claude" (Rich): analogía de la calculadora; las entrevistas técnicas van a cambiar `[00:15:55]`; Opus buen punto de partida pero caro `[00:17:15–00:17:29]`; "crear agentes no es el negocio, sino orquestar subagentes" `[00:20:12]`.
- `[00:22:07–00:22:33]` Créditos de 1,000 pesos por persona (el QR). Wi-Fi "Otoño 26" (?) `[00:22:55]`; la contraseña no se oye.

## Workshop 1 — temas en el orden en que se dieron

### 1. Presentación del ponente `[00:30:16–00:30:37]`
Ingeniero en Banco Santander; ~2 años en el banco y ~10 de carrera, casi todo en datos e ingeniería. Más tarde: construyen agentes para productos y procesos del banco `[00:36:35]`.

### 2. Por qué falla un tool call: variabilidad entre proveedores `[00:30:40–00:36:19]`
- Muestra OpenRouter y la métrica **tool call error rate** por proveedor para un mismo modelo `[00:31:31]`.
- Cifras citadas (modelo y unidades **inciertos**): un proveedor "OpenAI Flex" con 11.1% promedio `[00:31:46]`; Bedrock con máximo 0.44 y mínimo 0.15 `[00:32:03]`; un modelo open source "de 4.0" (?) con 17.3% `[00:33:27]`.
- Idea central: el mismo modelo, servido por distintos proveedores, da tasas de error muy distintas `[00:35:05]`.
- Dice que un **selector dinámico de proveedor** baja el error "de 8%" (?) para un GLM5 (?) `[00:35:15–00:35:44]`.
- Hipótesis de la audiencia `[00:33:51–00:34:34]`: saturación (Alexis), definición ambigua de la herramienta (Jonathan), cómo el proveedor ofrece el output estructurado, rate limit.
- Hipótesis del ponente `[00:35:52–00:36:09]`: **cuantización** y **decodificación restringida**; además capacidad del servicio / límites de tasa.

### 3. Logística del repo `[00:36:35–00:39:43]`
- Slides en su sitio web (HTML descargable), h1sort.com `[00:36:56, 00:49:33]`.
- Repo en su GitHub (h1sort); en el audio suena "Cloud Korea Engineering" (?), que coincide con `claude4aieng`. `git clone` en una carpeta `Code` `[00:39:30–00:39:43]`.

### 4. Entorno con uv `[00:40:19–00:42:40]`
- `uv sync`: instala 24 paquetes en 103 ms (parte en caché) y crea el entorno virtual `[00:40:58–00:41:14]`.
- `uv run` permite correr sin activar el entorno `[00:41:24]`; corre `scripts/check.py` `[00:41:33]`.
- `check.py` verifica Python (el suyo: 3.13.14 (?)), dependencias (Anthropic 1.15.0 (?)), SQLite con **datos ficticios** de un banco, la `ANTHROPIC_API_KEY` y una llamada mínima a Claude Sonnet 5.5 `[00:41:42–00:42:31]`. Termina con "Todo listo. Nos vemos el lunes." `[00:42:40]`.
- Comenta que uv es de Astral/Charlie Marsh y que fue comprada por OpenAI `[00:40:31–00:40:43]` (afirmación del ponente, no verificada).

### 5. Teoría: tokens y `tool_use` `[00:43:15–00:49:09]`
- Un modelo de lenguaje solo ve tokens `[00:43:17]`. Muestra el formato de **Qwen 3 (8B)** (?) `[00:43:37]`: `im_start`, un system prompt "eres un asistente del banco", las tools definidas en un pseudo-XML.
- En modelos **abiertos** se conocen los tokens especiales; en los **privados** no, porque se introducen en el aprendizaje por refuerzo posterior al preentrenamiento `[00:44:00–00:44:26]`. Se pueden ver en Hugging Face (`tokenizer_config`) `[00:46:12]`.
- Lo que sí se conoce con Claude es el **JSON** de la API: `stop_reason: tool_use`; un bloque `tool_use` con `id`, `name` (aquí `sql_query`) e `input`; y la respuesta como `tool_result` con ese id `[00:45:06–00:45:47]`. Ejemplo: el conteo devuelto fue 26.
- Un modelo abierto emite tokens y un **parser** los convierte en esa llamada estructurada `[00:44:34]`.
- Frameworks mencionados por la audiencia `[00:47:43–00:48:00]`: "Lanxime" (?), "Paidante" (?), Microsoft Agent Framework. Todos hacen lo mismo: parsean ese JSON y ejecutan las tools `[00:48:04–00:48:17]`.
- **Arnés (harness):** el código propio que parsea y ejecuta; "las tools completamente al desnudo" `[00:48:18–00:48:28]`.
- Tesis resumida `[00:48:50]`: la API entrega la llamada estructurada y la aplicación sigue ejecutando (el modelo propone, la aplicación ejecuta).

### 6. Ejercicio paso 0 `[00:49:09–00:51:57]`
1. Tener clonado el repo; `git checkout paso-0` `[00:49:46–00:49:55]`.
2. Correr el agente (agente de consulta del banco) y preguntar cuántas tarjetas bloqueadas hay `[00:50:33–00:50:43]`.
3. Resultado esperado: responde que no lo implementó, porque recibe el JSON pero **no hay código que lo lea** `[00:50:43–00:50:56]`.
4. Abrir `agent.py` (en un editor, nombre "Mission Studio" (?) `[00:50:56]`); lo demás ya está definido `[00:51:23–00:51:32]`.
5. **Tarea:** implementar en ~3 minutos un parser que decodifique la llamada del API y ejecute la tool `[00:51:35–00:51:51]`.

Ver [tareas.md](tareas.md) para el avance.

### 7. Instrucciones del ejercicio y tiempo `P2 [00:00:00–00:04:28]`
- Se puede usar cualquier agente (Claude Code, etc.) y pedirle que lea el código y el contexto `P2 [00:00:03]`.
- Lo único que hay que hacer: **implementar el uso de tools del agente, es decir, leer el JSON y ejecutar la llamada** `P2 [00:00:08]`; la tarea es el parsing del JSON que codifica la llamada `P2 [00:01:38]`.
- Se repite la dirección de las slides y el repo (h1sort.com / claude4aieng) `P2 [00:00:55–00:02:40]`; en el audio suena "cloud4.ai" (?) `P2 [00:02:28]`.
- Cuatro minutos para el ejercicio, regreso "a las 6:04" `P2 [00:03:07–00:03:12]`. Referencia al código: "la línea 180" de `agent.py` (?) `P2 [00:04:25–00:04:28]` (el `TODO(paso-1)` está cerca de esa línea).
- **Hueco sin grabar: 18:04–18:08.**

### 8. Solución y cierre `P3 [00:00:00–00:03:02]`
- La herramienta se ejecuta y se contesta con un bloque de sintaxis `type: tool_result`, `tool_use_id`, `content` `P3 [00:00:15–00:00:30]`.
- Significado: **recibo un JSON, lo leo y decido ejecutarlo** `P3 [00:00:39–00:00:48]`.
- **Lección principal:** el arnés de ejecución, hecho con LangChain (?) , con el SDK o con otra librería, usa primitivas de este estilo `P3 [00:00:48–00:01:02]`. Aunque esté muy automatizado, entender los internos "nos hace mejores ingenieros" (analogía de entender un carro) `P3 [00:01:05–00:01:19]`.
- Dice que movió más material del que pudo explicar; las slides se quedan en su sitio `P3 [00:01:30–00:01:41]`.
- **Recurso recomendado:** cmu-agents.com, curso de posgrado de Carnegie Mellon; se basó en el calendario de la **clase 2** (slides y grabaciones en YouTube) `P3 [00:01:52–00:02:21]`. Contacto: h1sort.com, Twitter `P3 [00:02:45]`.
- Entrega la palabra a Rich `P3 [00:02:54]`.

## Dudas abiertas

- Modelo(s) y unidades exactas de las cifras de OpenRouter (11.1%, 0.15–0.44, 17.3%).
- Nombre del modelo open source "de 4.0" y del "GLM5" `[00:32:24, 00:35:15]`.
- Versión de Python y de `anthropic` que mostró (3.13.14, 1.15.0) `[00:41:42, 00:41:52]`.
- Marcas de tiempo desordenadas entre `[00:26:01]` y `[00:26:30]` (zona de la encuesta, sin contenido técnico).
- Nombres de los frameworks de agentes que gritó la audiencia.
- Qué dijo el ponente entre las 18:04 y las 18:08 (no se grabó).
- Si "la línea 180" `P2 [00:04:28]` se refiere a `agent.py` (la transcripción lo deja dudoso).
