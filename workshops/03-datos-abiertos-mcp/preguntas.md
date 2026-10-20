# Preguntas para el ponente · Dante Bazaldua

**Solo tres.** Criterio: que apunten a su **experiencia haciendo de Spot2 una empresa "API/MCP first"** y dejen una lección general para cualquiera que conecte agentes con sus sistemas.
Marca con ✅ las que ya se hicieron y anota la respuesta debajo.
Las marcas `[hh:mm:ss]` apuntan a `transcripts/03-datos-abiertos-mcp/sesion.md`.

- [ ] **1. En Spot2 tratan a los agentes como usuarios de primera clase. ¿Qué cambió en cómo construyen producto y en cómo se organiza el equipo, y qué error evitarías si empezaras de nuevo?**
  Por qué: sirve a cualquier empresa que esté decidiendo si abrir sus sistemas a agentes. Contexto: los agentes navegan el sitio, piden citas y buscan información; casi todos los sistemas están conectados por MCP `[00:06:34–00:06:58]`.
- [ ] **2. Con muchas tools expuestas, ¿cómo evitan llenar el contexto y cómo saben que el agente elige bien? ¿Qué aprendiste de iterar tus tools y evaluaciones que no esperabas?**
  Por qué: junta los dos grandes costos de MCP (contexto y calidad de elección) en una lección práctica. Contexto: cada MCP añade un "texto gigante" de definiciones y dijo que refinan constantemente tools y evaluaciones `[00:12:48–00:13:05]` · `[00:30:03–00:30:36]` · `[00:38:03–00:38:16]`.
- [ ] **3. ¿Has visto un riesgo de seguridad real al dar acceso a agentes (permisos por usuario, *tool poisoning*, acciones que escriben)? ¿Qué controles pondrías desde el día uno?**
  Por qué: deja una lista de controles mínimos. Contexto: dijo que *tool poisoning* e *injection* siguen sin resolverse y que los controles van en el código `[00:13:33–00:13:42]` · `[00:27:02–00:28:30]`.

## Reserva (no se harán; por si sobra tiempo)

- ¿Cuántas tools son demasiadas antes de que moleste, y cargan tools bajo demanda? `[00:11:54–00:13:05]`
- ¿Cómo arman el *golden set* de evaluaciones (pedidos directos, indirectos y negativos) y cada cuánto lo corren? `[00:30:03–00:30:57]`
- OAuth por usuario: en el ejemplo de Sentry, ¿cómo se dividen los permisos en la práctica? `[00:12:09–00:12:48]`
- Composición: ¿cuándo prefieren escribir código que llame a las tools en vez de encadenar tool calls? `[00:13:15–00:13:33]`
- Idempotencia: ¿cómo la implementan en acciones que escriben y qué pasa si el modelo repite la llamada? `[00:28:01–00:28:13]`
- Skills frente a MCP: ¿cuándo empaquetan una skill junto al MCP? `[00:28:59–00:29:28]`
- De HTTP local a MCP remoto con OAuth: ¿qué cambia? `[00:16:26–00:16:55]`
- El concurso anunciado al inicio: ¿dónde están las bases y las fechas? `[00:00:21–00:01:10]`
