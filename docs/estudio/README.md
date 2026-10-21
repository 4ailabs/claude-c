# Ruta de estudio

Las cinco clases del evento, reorganizadas **por tema** y de lo más básico a lo más avanzado, para estudiarlas en orden y que dejen enseñanza. En lugar de seguir cada clase por separado, aquí se junta lo que dijeron los ponentes sobre cada idea.

## Cómo está armada

Seis módulos que se apoyan uno en el otro. Cada módulo tiene siempre lo mismo:

1. **Al terminar podrás…** (objetivos concretos)
2. **La idea en simple** (una analogía)
3. **Cómo funciona** (paso a paso)
4. **Lo que dijeron en las clases** (con la marca de tiempo para ir al detalle)
5. **Pruébalo tú** (un ejercicio que corre sin API ni créditos, y qué hacer con el repo del ponente)
6. **Errores comunes** y **preguntas de repaso** con respuestas
7. **Conecta con** el módulo anterior y el siguiente

## El orden

| # | Módulo | Pregunta que responde | Clase principal | Tiempo |
|---|---|---|---|---|
| 1 | [El agente actúa](01-el-agente-actua.md) | ¿Cómo hace algo un modelo si solo predice texto? | W1 · Carlos Haro | ~2 h |
| 2 | [El contexto](02-el-contexto.md) | ¿Qué ve el agente y qué pasa cuando se llena? | W2 · Alejandro Martínez | ~2 h |
| 3 | [MCP y diseño de tools](03-mcp-y-diseno-de-tools.md) | ¿Cómo se conecta con tus sistemas y cómo se diseñan bien las herramientas? | W3 · Dante Bazaldua | ~2.5 h |
| 4 | [Controles y seguridad](04-controles-y-seguridad.md) | ¿Cómo evito que haga daño o que lo manipulen? | W3, W5, W4 | ~2 h |
| 5 | [Mundo físico y enjambres](05-mundo-fisico-y-enjambres.md) | ¿Qué cambia cuando actúa en lo físico o con agentes ajenos? | W4 · Jonathan Olvera | ~1.5 h |
| 6 | [Evaluar y auditar](06-evaluar-y-auditar.md) | ¿Cómo mido y demuestro que funciona sin sesgos? | W5 · Jésica Tapia | ~2.5 h |

Aparte: el [glosario](00-glosario.md) (consúltalo cuando aparezca un término) y los [ejercicios](ejercicios) (seis scripts de Python, sin dependencias).

## De qué clase sale cada módulo

| Clase | Módulos donde se usa |
|---|---|
| **W1 · Tool use sin abstracciones** | **1** · también 6 |
| **W2 · Context engineering** | **2** · también 4 (barandillas al compactar) |
| **W3 · Datos abiertos over MCP** | **3** · también 4 y 6 |
| **W4 · Physical AI + MCP + Swarm** | **5** · también 4 |
| **W5 · Del agente al equipo** | **6** · también 4 y 5 (el video del enjambre) |

Las notas completas de cada clase (con las dudas) están en `workshops/NN-*/notas.md`.

## Cómo estudiar cada módulo (unas 2 horas)

1. **Lee** las secciones 1 y 2 (unos 30 minutos). Si aparece un término raro, búscalo en el glosario.
2. **Corre el ejercicio** de la sección 4 y léelo con calma: cada script es corto y comentado. Cambia algo y mira qué pasa (unos 20 minutos).
3. **Lee** "Lo que dijeron en las clases" y abre la nota de la clase si quieres el contexto de una cita.
4. **Responde** las preguntas de repaso **sin mirar** las respuestas, y luego compáralas (15 minutos).
5. **Explícalo en voz alta**, como si se lo contaras a alguien. Si te trabas, vuelve a la sección que falló.
6. Al día siguiente, repasa solo las preguntas.

## Un calendario posible

| Sesión | Módulo | Producto de la sesión |
|---|---|---|
| 1 | 1 · El agente actúa | Puedes explicar `tool_use` / `tool_result` con tus palabras |
| 2 | 2 · El contexto | Sabes cuándo compactar con referencia y cuándo no |
| 3 | 3 · MCP y diseño de tools | Reescribes una tool mala como una buena |
| 4 | 4 · Controles y seguridad | Listas los controles de una tool que escribe |
| 5 | 5 · Mundo físico y enjambres | Defines umbrales y cuándo entra un humano |
| 6 | 6 · Evaluar y auditar | Haces una prueba con pares y lees el resultado |
| 7 | Repaso | Respondes las preguntas de los seis módulos sin ayuda |

## Lo que necesitas

- **Para los ejercicios y las lecturas:** solo `python3`. No hace falta internet, API ni créditos.
- **Para practicar con los repos de los ponentes** (opcional): `uv`, y para algunos una **API key con créditos**. Ver el estado de cada uno en [`workshops/README.md`](../../workshops/README.md).

## Cuando termines, deberías poder…

- [ ] Explicar quién ejecuta una tool y qué lleva un `tool_result`.
- [ ] Describir el ciclo de un arnés y por qué falla un tool call.
- [ ] Decir de qué se compone el contexto y qué es el *context rot*.
- [ ] Comparar compactar sin y con referencia, y decidir cuándo no compactar.
- [ ] Elegir entre MCP, CLI y API.
- [ ] Rediseñar una tool genérica como una por intención, con errores que enseñan.
- [ ] Nombrar cuatro controles de código para una tool que escribe.
- [ ] Reconocer una *prompt injection* y por qué todo texto externo es no confiable.
- [ ] Explicar cómo se definen umbrales y humano en el loop para algo físico.
- [ ] Hacer una prueba de sesgo con pares y explicar el resultado.

## Más allá

- [Mapa de conceptos](../conceptos.md): los 23 conceptos, uno por uno, con las citas de cada ponente.
- [Guía final](../guia-final.md): el resumen del evento.
- Tres preguntas para cada ponente, sobre su experiencia, en `workshops/NN-*/preguntas.md`.
- Para profundizar en tool use: el curso 11-768 AI Agents de Carnegie Mellon, **clase 2** (`cmu-agents.com`), que recomendó el ponente del W1.
