# Módulo 1 · El agente actúa: tools, arnés y por qué fallan

**Tiempo:** unas 2 horas · **Prerrequisitos:** ninguno · **Clase principal:** workshop 1 (Carlos Haro) · **También:** W3

## Al terminar podrás

- Explicar qué es una **tool** y quién ejecuta qué.
- Leer un `tool_use` y escribir el `tool_result` correcto.
- Explicar qué es un **arnés** y por qué un framework no lo reemplaza.
- Enumerar por qué falla un tool call y cómo se mide.

## 1. La idea en simple

Un modelo es como un cliente que **solo puede escribir pedidos en un papel**. No cocina. Tu código es la cocina: lee el pedido, lo prepara y devuelve el plato. A ese ciclo, completo, se le llama **arnés**.

> **El modelo propone, la aplicación ejecuta, y eso se mide.** Es la tesis de todo el evento.

## 2. Cómo funciona, paso a paso

1. Le das al modelo una pregunta y la **lista de tools** que existen (nombre, descripción, parámetros).
2. El modelo no ejecuta nada. Responde con un bloque que dice "quiero esta tool con estos datos":

```json
{"stop_reason": "tool_use",
 "content": [{"type": "tool_use", "id": "toolu_01", "name": "sql_query",
              "input": {"sql": "SELECT COUNT(*) FROM tarjetas WHERE estado='bloqueada'"}}]}
```

3. **Tu código** lee ese JSON (lo *parsea*), ejecuta la función y obtiene un resultado.
4. Se lo devuelves en **un solo mensaje de usuario**, con **un `tool_result` por cada llamada**, usando el mismo `id`:

```json
{"role": "user", "content": [{"type": "tool_result", "tool_use_id": "toolu_01", "content": "26"}]}
```

5. El modelo lee el resultado y responde con texto (`stop_reason: end_turn`) o pide otra tool. Si pide otra, repite desde el 3.

**Regla de oro:** cada `tool_use` necesita su `tool_result` en el mensaje siguiente. Si falta, la API responde con error 400.

## 3. Lo que dijeron en la clase (W1)

- Un modelo "solo tiene tokens". De un modelo **abierto** (como Qwen) se conocen los tokens especiales; de uno **privado** no, porque se introducen en el aprendizaje por refuerzo posterior al preentrenamiento. Lo que sí se ve de uno privado es el **JSON** de la API `[00:43:15–00:44:26]`.
- Los frameworks (LangChain (?), Pydantic AI (?), Microsoft Agent Framework) hacen lo mismo: **parsean ese JSON y ejecutan las tools** `[00:47:43–00:48:17]`. Lección final: se haga con un framework o con el SDK, **el arnés usa estas primitivas**; entenderlo "te hace mejor ingeniero", como entender un carro mejor te hace mejor conductor `W1·P3 [00:00:48–00:01:19]`.
- **Los tool calls fallan distinto según el proveedor** que sirve el mismo modelo. Mostró tasas de error de 11.1%, 0.15–0.44 y 17.3% (modelo y unidades dudosos) `[00:31:31–00:33:27]`.
- Por qué (hipótesis): saturación, definición ambigua de la tool, cómo se ofrece el output estructurado, rate limit, **cuantización** y **decodificación restringida** `[00:33:51–00:36:09]`. Un selector dinámico de proveedor bajó los errores `[00:35:15–00:35:44]`.
- En el repo del taller se rompe el agente a propósito de tres formas: un `tool_use` **huérfano** (sin resultado), un JSON **truncado** por `max_tokens` y una llamada **válida pero peligrosa**.

## 4. Pruébalo tú

**Sin gastar nada** (solo Python):

```bash
python3 docs/estudio/ejercicios/01_mini_arnes.py
```

Verás el arnés completo y luego el error de "tool_use sin tool_result". Abre el archivo, lee `agente()` y ubica dónde el modelo **propone** y dónde el código **ejecuta**.

**Con el repo del workshop** (`workshops/01-tool-use-sin-abstracciones/claude4aieng`): `uv run pytest -q` y lee el paso 1 en `taller/agent.py`. Con una API key con créditos, `uv run python -m taller.agent` y pregunta «¿cuántas tarjetas bloqueadas hay?» (respuesta: 26).

## 5. Errores comunes

- Pensar que el modelo "ejecuta" la herramienta. Solo la pide.
- **Olvidar un `tool_result`** (error 400) o devolver los resultados en mensajes separados.
- **Ejecutar un JSON truncado** (el modelo se quedó sin `max_tokens` a mitad de la llamada). Se descarta y se reintenta con más margen.
- Culpar siempre al modelo: parte del error es del proveedor o de tu definición de la tool.

## 6. Preguntas de repaso

1. ¿Quién ejecuta la herramienta, el modelo o tu código?
2. ¿Qué dos campos del `tool_use` usas para armar el `tool_result`?
3. ¿Por qué un tool call puede fallar aunque el modelo sea bueno?
4. ¿Qué es un arnés y qué hace un framework respecto a él?

<details><summary>Respuestas</summary>

1. Tu código. El modelo solo la pide.
2. El `id` (que vuelve como `tool_use_id`) y el `name`/`input` para saber qué ejecutar.
3. Por el proveedor (saturación, cuantización, rate limit), por una definición ambigua de la tool o por salidas con forma incorrecta.
4. El código que ejecuta el ciclo pedir → ejecutar → responder. Un framework lo trae hecho; entender el ciclo te permite depurarlo.
</details>

## 7. Conecta con

- Siguiente: [Módulo 2 · El contexto](02-el-contexto.md). Cada definición de tool ocupa contexto.
- Mide la tasa de error en el [Módulo 6](06-evaluar-y-auditar.md).
- Términos: [glosario](00-glosario.md). Conceptos 1 a 4 de [conceptos.md](../conceptos.md).
