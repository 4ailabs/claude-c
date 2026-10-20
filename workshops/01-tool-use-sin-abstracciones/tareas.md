# Tareas y ejercicios

Código en el repo del ponente: `workshops/01-tool-use-sin-abstracciones/claude4aieng` (rama `paso-0`, https://github.com/h1sort/claude4aieng).
Aquí queda la consigna, el plan y el avance.

## Consigna

Fuente: `[00:49:09–00:51:57]` de la sesión y `BRANCH.md` de la rama `paso-0`.

**Paso 1 — el bucle.** En `taller/agent.py`, dentro de `Agent.run`, busca `# TODO(paso-1)`:
ejecuta las llamadas con `execute_calls` y contesta con **un solo mensaje de usuario** con **un `tool_result` por llamada**
(con su `tool_use_id`, antes de cualquier texto; `is_error` solo si falló).

Comprobación: `uv run python -m taller.agent` y preguntar «¿cuántas tarjetas bloqueadas hay?». Respuesta esperada: **26**.
Sin el paso 1 el agente falla con `NotImplementedError` porque recibe el JSON `tool_use` pero no hay código que lo lea.

## Plan

1. Ejecutar `turn.calls` con `execute_calls(turn.calls, self.tools)` (corre en paralelo y conserva el orden).
2. Armar un mensaje `{"role": "user", "content": [tool_result, ...]}` con un bloque por resultado.
3. Guardar `turn.results` (ya lo hace el código que sigue) y dejar que el bucle haga la siguiente petición.
4. No tocar los demás `TODO`: `paso-2` (huérfanos), `paso-3` (JSON truncado) y `paso-4` (compuerta SQL) son ejercicios posteriores.

## Avance

- [x] **Paso 1 escrito** en `taller/agent.py` (cambio sin commitear en `claude4aieng`, rama `paso-0`):

```python
# paso-1: la aplicación ejecuta lo que el modelo propuso y contesta con UN mensaje de usuario:
# un tool_result por llamada, con su tool_use_id, en el mismo orden; is_error solo si falló.
results: list[ToolResult] = await execute_calls(turn.calls, self.tools)
messages.append({"role": "user", "content": [
    {"type": "tool_result", "tool_use_id": r.tool_use_id, "content": r.content}
    | ({"is_error": True} if r.is_error else {})
    for r in results]})
turn.results = results
```

  Se quitó el `raise NotImplementedError` de paso-1, que ya no aplica.
  Equivale a la solución oficial de `origin/paso-1` (comparada leyendo `git diff paso-0 origin/paso-1`; la oficial usa `**{...}` en lugar de `|`).
- [ ] **Sin verificar en ejecución.** No pude correr `pytest` ni el agente desde esta sesión. Falta correr:
  - `uv run pytest -q` (los pasos 2–4 deben salir *skipped*; los de paso-1 deben pasar)
  - `uv run python -m taller.agent` → «¿cuántas tarjetas bloqueadas hay?» → 26
- [ ] Siguientes: `paso-2` (sanear historial con `tool_use` huérfano y `paso-2b` timeout en paralelo), `paso-3`, `paso-4`.
