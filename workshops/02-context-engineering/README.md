# Context engineering

**Ponente:** Alejandro Martínez (Sr Software Engineer, Platzi)

Compactación y descubrimiento dinámico de contexto y tools.

## Sales con

- Un agente con Pydantic AI que resume su contexto para continuar una tarea.
- Búsqueda y carga de información de archivos en disco.
- Carga de las herramientas que necesita, cuando las necesita.
- Una comparación de qué información conserva y cuánto contexto usa.

## En una frase

El contexto es finito y se degrada; compactar con una referencia al original en disco evita perder los detalles.

## Lo esencial

- *Context rot*: la calidad cae mucho antes de la ventana anunciada.
- Compactar **sin** referencia pierde detalles; **con** referencia deja un puntero al original y el agente lo busca con `search_file` y `read_file`.
- Otras técnicas: truncar, limpiar resultados de tools, notas, subagentes. Los sistemas multiagente cuestan más contexto.

## Qué hay en esta carpeta

| Archivo | Para qué |
|---|---|
| [`notas.md`](notas.md) | Lo que se dijo, en orden, con marcas `[hh:mm:ss]` y las dudas marcadas con (?) |
| [`preguntas.md`](preguntas.md) | Las **tres preguntas** para el ponente, sobre su experiencia (y una reserva) |
| [`tareas.md`](tareas.md) | La consigna, el plan y el avance de la práctica |
| [`context-engineering-workshop/`](context-engineering-workshop) | Repo del ponente ([alexMtzRivero/context-engineering-workshop](https://github.com/alexMtzRivero/context-engineering-workshop)), rama `main`; **no se versiona aquí** |
| Transcripción | `transcripts/02-context-engineering/`, **no se versiona** (lleva voces de asistentes) |

## Para retomarlo

```bash
cd workshops/02-context-engineering/context-engineering-workshop
.venv/bin/python -m unittest discover -s tests            # 17 de 27 pasan; los 10 restantes son de los pasos 3 a 5
.venv/bin/python -m uvicorn app:app --host 127.0.0.1 --port 8000   # http://127.0.0.1:8000
```

> Usa **siempre** `.venv/bin/python`: tu `~/.zshrc` define `alias python=python3.11`, que ignora el entorno virtual.
> Para el chat necesitas un `.env` con `MODEL=anthropic:claude-haiku-5-5` y `ANTHROPIC_API_KEY=...` (la escribes tú, con créditos).

Siguiente: `paso3_compactacion.py`, `paso4_descubrimiento.py` y `paso5_subagente.py`. La rama `solucion` los trae resueltos (`git diff main solucion -- paso3_compactacion.py`).

## Estado

- [x] Notas, preguntas y tareas.
- [x] **Paso 2** (`list_files`, `read_file`, `search_file`, `write_file`) escrito y probado.
- [x] Entorno `.venv` con Python 3.14 funcionando.
- [ ] Pasos 3, 4 y 5.
- [ ] Probar el chat con una API key **con créditos**.

**Para estudiar este tema:** [Módulo 2 · El contexto](../../docs/estudio/02-el-contexto.md).

Ver también: [guía final](../../docs/guia-final.md) · [conceptos](../../docs/conceptos.md) · [temario](../../docs/temario.md).
