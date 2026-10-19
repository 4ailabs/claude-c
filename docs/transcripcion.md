# Grabar y transcribir

1. Graba cada workshop como un archivo aparte y guárdalo en `recordings/`
   (está en `.gitignore`: son pesados y tienen la voz de los asistentes).
2. Copia `.env.example` a `.env` y escribe `MISTRAL_API_KEY`. **No** pegues la
   clave en el código, en issues ni en commits.
3. Transcribe:

   ```bash
   uv run tools/transcribe.py recordings/w1.m4a \
     --out transcripts/01-tool-use-sin-abstracciones/sesion.md
   ```

   Salen `sesion.md` (legible, con marcas de tiempo) y `sesion.json` (respuesta cruda por trozo).

Notas:

- Requiere `ffmpeg` y `uv`. El audio se corta en trozos de 10 min (`--chunk-minutes`),
  mono 16 kHz, para no pasar de los límites de la API; las marcas de tiempo son
  el inicio del trozo más el desplazamiento del segmento.
- `--dry-run` solo corta y lista los trozos, sin llamar a la API ni necesitar clave.
- `--timestamps` pide marcas por segmento. En ese modo no se envía `--language`
  (la API no permite ambos); sin él se fuerza español.
- El modelo por defecto es `voxtral-mini-latest`; cámbialo con `--model`.
