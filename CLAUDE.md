# Contexto del repo

Repo personal para seguir el evento *Claude for AI Engineering* (CDMX): 5 workshops
técnicos. Temario en `docs/temario.md`; flujo en `docs/flujo.md`.

## Qué se espera de ti

- **Transcribir**: `uv run tools/transcribe.py <audio> --out transcripts/<workshop>/sesion.md`.
  La clave está en `.env` (`MISTRAL_API_KEY`); nunca la imprimas ni la subas a git.
- **Procesar** una transcripción: escribe `workshops/<n>/notas.md` con los temas en el
  orden en que se dieron, decisiones técnicas, código/comandos mencionados y dudas abiertas.
  Cita la marca de tiempo `[hh:mm:ss]` de donde sale cada punto. No inventes lo que no se dijo;
  marca como incierto lo que la transcripción deja dudoso (nombres, cifras, términos técnicos).
- **Preguntas**: propón en `preguntas.md` las más valiosas, ordenadas por prioridad.
- **Tareas**: ayuda a resolver lo que pidan, en la carpeta del workshop.
- Idioma: español. Las grabaciones (`recordings/`) y `.env` no se versionan.
