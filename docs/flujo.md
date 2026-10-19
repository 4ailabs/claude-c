# Flujo de trabajo del evento

1. **Grabar** cada workshop como un archivo aparte en `recordings/` (ignorado por git).
2. **Transcribir** (ver [transcripcion.md](transcripcion.md)):
   `uv run tools/transcribe.py recordings/<archivo> --out transcripts/<workshop>/sesion.md`
3. **Procesar** la transcripción en `workshops/<n>/notas.md`: temas en orden, decisiones
   técnicas, código y comandos mencionados, conceptos clave y dudas abiertas.
4. **Preguntas** para el ponente en `workshops/<n>/preguntas.md`, por prioridad: lo ambiguo,
   los casos límite y los "¿por qué así y no de otra forma?".
5. **Tareas**: si piden un trabajo o ejercicio, la consigna va en `workshops/<n>/tareas.md`
   y el código en la misma carpeta.
6. **Cierre**: consolidar todo en una guía única del evento (`docs/guia-final.md`).
