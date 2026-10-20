# Preguntas para el ponente · Carlos Haro

**Solo tres.** Criterio: que apunten a su **experiencia construyendo agentes en un banco** y dejen una lección general para cualquiera que construya agentes.
Marca con ✅ las que ya se hicieron y anota la respuesta debajo.
Las marcas `[hh:mm:ss]` apuntan a `transcripts/01-tool-use-sin-abstracciones/sesion.md` (las `P3`, a `sesion-parte3.md`).

- [ ] **1. En producción, dentro de un banco, ¿cuál fue el fallo de tool use que más te sorprendió o más costó, y qué cambió en cómo diseñas y mides tus agentes desde entonces?**
  Por qué: enseña qué errores esperar en la práctica y no solo en la teoría. Contexto: construyen agentes para productos y procesos del banco `[00:36:35]`; mostró tasas de error de tool call muy distintas según el proveedor `[00:31:31–00:33:27]`.
- [ ] **2. Al elegir un modelo o un proveedor para un agente, ¿qué mides antes de confiar en él (tasa de error de tools, costo por tarea, latencia) y qué resultado te haría cambiar de opinión?**
  Por qué: deja un criterio de decisión que se puede reutilizar. Contexto: el mismo modelo falla distinto según el proveedor, y un selector dinámico bajó los errores `[00:35:05–00:35:44]`.
- [ ] **3. Si alguien empieza hoy a construir su primer agente: ¿cuándo vale la pena escribir el arnés a mano y cuándo usar un framework o el Tool Runner? ¿Qué aprendiste a mano que no habrías aprendido de otra forma?**
  Por qué: orienta a quien está aprendiendo. Contexto: su lección final fue que todo arnés usa estas primitivas `P3 [00:00:48–00:01:19]`.

## Reserva (no se harán; por si sobra tiempo)

- ¿Qué cuenta exactamente como "error de tool call" en OpenRouter y en qué unidades eran las cifras (11.1%, 0.15–0.44, 17.3%)? `[00:31:31–00:33:27]`
- ¿La decodificación restringida (`strict: true`) elimina la variabilidad entre proveedores o solo valida la forma? `[00:35:52–00:36:09]`
- ¿Cuánto del error es del proveedor y cuánto de tu propio código? `[00:34:59–00:35:44]`
- Con modelos abiertos, ¿quién garantiza que el parser del proveedor corresponde a los tokens del modelo? `[00:44:34]`
- ¿Hay una forma estándar de saber si un proveedor cuantiza el modelo? `[00:35:52]`
- Datos "ficticios" del banco: ¿qué tan fiel debe ser un SQLite de prueba para que la tasa medida se parezca a producción? `[00:42:00]`
