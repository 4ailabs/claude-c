# Módulo 4 · Controles y seguridad

**Tiempo:** unas 2 horas · **Prerrequisitos:** módulos 1 a 3 · **Clases:** W3 (Dante), W5 (Jésica), W4 (Jonathan)

## Al terminar podrás

- Explicar por qué los controles van **en el código** y no en el prompt.
- Nombrar cuatro controles para una tool que escribe.
- Reconocer una *prompt injection* y por qué todo texto externo es entrada no confiable.
- Describir qué es una **barandilla** y dónde se pone.

## 1. La idea en simple

Un modelo es como un empleado muy capaz que **a veces se equivoca o se deja convencer**. No le pidas "por favor no abras la caja fuerte" y listo: **ponle cerradura a la caja fuerte**. La cerradura es código; no se deja convencer.

## 2. Cómo funciona

**Cuatro controles para una tool que escribe** `W3 [00:27:02–00:28:30]`:

| Control | Qué hace |
|---|---|
| **Esquema cerrado** | Tipos y límites estrictos (p. ej. texto de 10 a 500 caracteres); lo que no cumple, se rechaza. |
| **Validación determinista** | El código comprueba reglas; "no es Claude, no es ningún otro modelo que se pueda inventar cosas". |
| **Idempotencia** | Repetir la llamada no duplica el efecto: devuelve el mismo folio. |
| **Aprobación humana** | La tool se marca para que el host pregunte a la persona antes de ejecutarla. |

Además, los *hints* del protocolo (como "solo lectura") le dicen a Claude si necesita pedir permiso `[00:21:27–00:22:35]`. Según el PDF, **son pistas, no garantías**: el control de verdad es el código.

**Entrada no confiable.** Todo texto que llega de fuera puede traer instrucciones escondidas:
- El resultado de una tool o la descripción de un MCP ajeno (*tool poisoning*) `W3 [00:13:33]`.
- Un **CV con una instrucción oculta** para el LLM `W5 [00:36:01–00:36:56]`.
- Un agente desconocido que entra a tu sistema `W4 [00:19:45–00:20:35]`.

**Barandillas** `W5 [00:18:30–00:18:55]`: reglas a la **entrada** y a la **salida**. En el caso de los CVs: el sistema **nunca recomienda a quién contratar** y **no puede inventar** lo que el CV no dice `[00:29:14–00:30:22]` · `[00:32:05]`.

**En capas** (video del W4, `W5 [00:01:49–00:02:45]`): un filtro rápido antes del modelo grande, un **mandato firmado** donde el modelo solo propone y los compromisos necesitan la firma de la persona, y mensajes firmados con identidad.

## 3. Lo que dijeron en las clases

- **W3:** el modelo "puede intentar un montón de cosas"; si una tool hace un `INSERT`, hay que pensar en qué validar para que nadie fuerce algo dañino `[00:27:10–00:27:35]`.
- **W4:** "¿qué pasa cuando se trata de una **válvula**?". La responsabilidad cae en el ingeniero; por eso parámetros y **un humano en el loop** `[00:09:40–00:10:05]`. Cierre: el humano aprueba o rechaza desde el celular `[00:34:20–00:35:13]`.
- **W5:** si el orquestador compacta mal el contexto, **se pueden perder las barandillas** `[00:20:01–00:20:21]`; conviene **definir todos los agentes y barandillas en un solo lugar** para poder encontrarlos `[00:25:57–00:26:38]`.

## 4. Pruébalo tú

**Sin gastar nada:**

```bash
python3 docs/estudio/ejercicios/04_controles_en_codigo.py
```

Una tool `registrar_reporte` con los cuatro controles: rechaza un texto corto, rechaza sin aprobación, registra una vez, devuelve el mismo folio al repetir y se frena sola en un ciclo. Cambia un control y observa qué deja pasar.

**Con el repo del W3:** en el paso 3, pide «Levanta un reporte: el elevador de Pantitlán, Línea A, no funciona». Claude Code pedirá aprobación; repítelo y verás el mismo folio. No pongas datos personales reales.

## 5. Errores comunes

- Poner el control solo en el prompt ("no hagas X").
- Confiar en que un *hint* impide algo.
- Tratar el texto devuelto por una tool o por un usuario como si fuera tuyo.
- Perder las barandillas al compactar o al repartir contexto entre agentes.
- Un humano en el loop que aprueba sin ver nada.

## 6. Preguntas de repaso

1. ¿Por qué un control en el código es más fuerte que uno en el prompt?
2. ¿Qué hace que una tool sea idempotente?
3. Da un ejemplo de *prompt injection* visto en las clases.
4. ¿Dónde se ponen las barandillas?

<details><summary>Respuestas</summary>

1. El código es determinista y no se deja convencer ni inventa; el modelo puede equivocarse o ser manipulado.
2. Que repetir la misma llamada no duplica el efecto (devuelve el mismo resultado o folio).
3. Un candidato que esconde una instrucción para el LLM en su CV (W5).
4. A la entrada y a la salida del sistema, y definidas en un solo lugar.
</details>

## 7. Conecta con

- Anterior: [Módulo 3](03-mcp-y-diseno-de-tools.md). Siguiente: [Módulo 5 · Mundo físico y enjambres](05-mundo-fisico-y-enjambres.md).
- Auditar y medir estos controles: [Módulo 6](06-evaluar-y-auditar.md).
- Conceptos 13, 14, 19 y 21 de [conceptos.md](../conceptos.md).
