# Preguntas para el ponente · Alejandro Martínez

**Solo tres.** Criterio: que apunten a su **experiencia con sistemas en producción en Platzi** y dejen una lección general para cualquiera que construya agentes de larga duración.
Marca con ✅ las que ya se hicieron y anota la respuesta debajo.
Las marcas `[hh:mm:ss]` apuntan a `transcripts/02-context-engineering/sesion.md`.

- [ ] **1. Dijiste que al preparar esta práctica descubriste que algunos sistemas de producción de Platzi se verían muy afectados por el *context rot*. ¿Qué síntoma te hizo notarlo, qué cambiaron y qué le dirías a alguien que aún no lo ha medido en su sistema?**
  Por qué: lleva la teoría a un caso real y enseña a detectarlo. Contexto: `[00:10:41–00:10:57]` (la transcripción es confusa en este tramo).
- [ ] **2. De todas las técnicas de contexto que has probado (truncar, resumir, notas, disco, subagentes), ¿cuál ha sobrevivido a varios modelos y cuál abandonaste? ¿Por qué?**
  Por qué: da un criterio de qué técnicas envejecen bien y cuáles no. Contexto: la compactación con referencia al disco "ha sobrevivido varios modelos" y el resumen estructurado no lo recomienda `[00:24:20–00:24:50]`.
- [ ] **3. ¿Cómo decides cuándo NO compactar y qué mides para saber si compactar te ayudó o te hizo daño (caché, costo, calidad de las respuestas)?**
  Por qué: deja un método de decisión y no una receta. Contexto: dijo que en producción compactar puede romper la caché y subir costos, y que el umbral depende del sistema `[00:29:53–00:30:59]`.

## Reserva (no se harán; por si sobra tiempo)

- Con referencia, ¿cómo evitas que el agente no busque en el archivo cuando debería? ¿Basta el puntero? `[00:19:41–00:19:51]`
- Subagentes por cliente frente a un agente que busca en disco: ¿cuándo uno y cuándo otro, y cómo se comparan en costo y exactitud? `[00:25:40–00:28:12]`
- ¿Qué benchmark y qué modelo midieron la degradación desde ~128 mil tokens? `[00:05:13–00:06:21]`
- El prompt del resumen es "mediocre": ¿qué instrucciones mejoran más la conservación de detalles? `[00:13:53–00:14:39]`
- Resumen estructurado: ¿hay algún caso donde sí lo usarías? `[00:24:20–00:24:34]`
- Multiagente usa más contexto que un solo agente: ¿en qué estudio se basa? `[00:07:40–00:08:13]`
- ¿Cómo decide el agente qué guardar como "nota" y qué descartar? `[00:23:12–00:23:41]`
- No se cubrió "tools bajo demanda" (paso 4): ¿cuándo reduce más contexto que compactar? `[00:01:45, 00:25:13]`
