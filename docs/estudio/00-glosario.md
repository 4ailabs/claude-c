# Glosario

Los términos del evento, en palabras sencillas. Entre paréntesis, el módulo donde se explican a fondo.

| Término | Qué significa |
|---|---|
| **Agente** | Un modelo que repite un ciclo: pide una herramienta, lee el resultado y decide el siguiente paso, hasta resolver la tarea. (1) |
| **Arnés (*harness*)** | El código que lee lo que el modelo pidió, lo ejecuta y le devuelve el resultado, en bucle. Un framework es un arnés ya hecho. (1) |
| **Atributo protegido** | Una característica que la ley protege de la discriminación (el género, por ejemplo). No debe influir en una decisión. (6) |
| **Barandilla (*guardrail*)** | Una regla puesta a la entrada o a la salida del sistema que limita lo que puede hacer o decir. (4) |
| **Bitácora** | Registro de lo que hizo el sistema. Con **hash** encadenado, se nota si alguien lo edita. (5, 6) |
| **Compactación** | Reemplazar un historial largo por un resumen más corto. (2) |
| **Contexto** | Todo lo que el modelo ve al responder: instrucciones, definiciones de tools, el chat, resúmenes y lo que se buscó. (2) |
| **Context rot** | La calidad del modelo se degrada cuando el contexto se llena, mucho antes del límite anunciado. (2) |
| **Decodificación restringida** | Forzar al modelo a producir solo salidas con cierta forma (por ejemplo, un JSON válido). (1) |
| **Eval (evaluación)** | Casos reales con la respuesta esperada, para medir si el sistema o el modelo hace lo correcto. (6) |
| **Golden set** | El conjunto de casos de una evaluación: pedidos directos, indirectos y negativos, con lo esperado. (6) |
| **Hash** | Una "huella" calculada a partir de un texto; si el texto cambia, la huella cambia. (5, 6) |
| **Humano en el loop** | Una persona aprueba o rechaza antes de que el sistema actúe. (4, 5) |
| **Idempotente** | Repetir la misma llamada no duplica el efecto: devuelve el mismo resultado (el mismo folio). (4) |
| **JSON** | Formato de texto con datos organizados (`{"nombre": "valor"}`), que un programa puede leer. (1) |
| **LLM** | Modelo de lenguaje: dado un texto, predice el siguiente token. Por sí solo no consulta ni ejecuta nada. (1) |
| **MCP** | Estándar abierto para conectar apps de IA (el host) con herramientas y datos (el servidor). (3) |
| **Host, cliente, servidor (MCP)** | El host es la app donde hablas (Claude Code); el cliente, el conector que crea; el servidor, el programa que expone tools, resources y prompts. (3) |
| **Orquestador / subagente** | El orquestador reparte el trabajo; cada subagente resuelve una parte con su propio contexto. (2) |
| **OAuth** | Mecanismo para que cada persona entre con su cuenta y con sus propios permisos. (3) |
| **Parser** | Código que lee un texto y lo convierte en datos que el programa usa. (1) |
| **Physical AI** | Agentes que operan en el mundo físico mediante hardware (cámaras, sensores, actuadores). (5) |
| **Prompt injection** | Texto que intenta darle instrucciones al modelo desde un lugar que no es el tuyo (un CV, una página, un resultado de tool). (4) |
| **Puntero / referencia** | Una indicación de dónde está el original (una ruta de archivo) para ir a buscar un detalle. (2) |
| **Rate limit** | El tope de llamadas que un proveedor deja hacer en un periodo. (1) |
| **Resource, prompt (MCP)** | Resource: un dato de solo lectura con dirección. Prompt: una plantilla de instrucciones que tú eliges ejecutar. (3) |
| **Schema (esquema)** | La descripción de los parámetros de una tool: tipos, límites y descripciones. (3) |
| **Sesgo de automatización** | Tendencia humana a no cuestionar lo que recomienda un sistema. (6) |
| **Skill** | Una carpeta con instrucciones que enseñan al agente a usar bien una herramienta; se carga solo cuando hace falta. (3) |
| **`stop_reason`** | El campo de la respuesta que dice por qué el modelo se detuvo (por ejemplo, `tool_use` o `end_turn`). (1) |
| **Swarm (enjambre)** | Varios agentes, de distintas personas, que se comunican y se coordinan. (5) |
| **Token** | Un trozo de texto (unas pocas letras) que es la unidad con la que trabaja el modelo y con la que se cobra. (1) |
| **Tool (herramienta)** | Una función con nombre, descripción y parámetros que el modelo puede **pedir** que se ejecute. (1) |
| **`tool_use` / `tool_result`** | El bloque con el que el modelo pide una tool, y el bloque con el que tu código le devuelve el resultado. (1) |
| **Tool poisoning** | Meter instrucciones maliciosas en la descripción o el resultado de una tool para manipular al modelo. (4) |
| **Transporte (MCP)** | Por dónde viajan los mensajes: `stdio` (el host lanza el programa) o HTTP (local o remoto). (3) |
