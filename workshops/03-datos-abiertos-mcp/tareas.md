# Tareas y ejercicios

Código en el repo del ponente: `workshops/03-datos-abiertos-mcp/claude-mcp-ibero-2026` (https://github.com/danteese/claude-mcp-ibero-2026).
Aquí queda la consigna, el plan y el avance.

## Consigna

Sección **"Construyamos"** del PDF (`datos-mcp-ibero.pdf`) y de la sesión `[00:17:08–00:34:47]`: cuatro pasos, cada uno con su comprobación.

1. **Una tool** — levantar `uv run servidor.py`, abrir `claude` en el repo y preguntar «¿Qué datos abiertos hay sobre bicicletas?» `[00:19:30–00:20:45]`.
2. **Diseño** — `cp pasos/02_consulta.py servidor.py`, reiniciar, reconectar y preguntar por Pantitlán en julio de 2026 (4,623,233) y por «insurgente» mal escrito `[00:24:11–00:24:59]`.
3. **Una acción** — `cp pasos/03_accion.py servidor.py`; pedir un reporte, aprobar, repetir (mismo folio) y probar la Línea 2 `[00:27:02–00:28:53]`.
4. **Medir y mapa** — `cp pasos/04_final.py servidor.py`; Ecobici cerca de Insurgentes y actualizar el mapa `[00:31:00–00:32:25]`.
- Cada paso: copiar → `Ctrl-C` y reiniciar el servidor → `/mcp → cdmx → Reconnect` → `uv run verificar.py N`.
- **Para llevarse:** usar otros datos (calidad del aire, 0311), crear otra tool y otra vista `[00:35:39–00:36:01]`.

## Plan

1. Preparar el entorno: `uv run preparar.py` y `uv run verificar.py`.
2. Copiar y verificar los pasos 2, 3 y 4.
3. Conectar `cdmx` en Claude Code y probar las preguntas de cada paso.
4. Opcional: correr `uv run evaluar.py` (gasta cuota de Claude) y probar los retos.

## Avance

- [x] Repo clonado; `preparar.py` generó `datos/cdmx.sqlite` (38,804 filas) y `verificar.py` pasó en verde.
- [x] **Pasos 2, 3 y 4 copiados a `servidor.py`** y comprobados con `verificar.py` (todo en orden). `servidor.py` quedó como el punto de control del paso 4: 8 tools, un resource y un prompt.
- [x] Servidor corriendo en segundo plano (`127.0.0.1:8765`), con las 8 tools verificadas como cliente MCP.
- [ ] **Conectar `cdmx` en Claude Code:** en `/mcp` aparece desactivado (`◯`); falta elegir **Enable/Reconnect**. La causa es `disabledMcpServers = ["cdmx"]` en `~/.claude.json` para este proyecto.
- [ ] Probar las preguntas de cada paso dentro de Claude Code.
- [ ] `uv run evaluar.py`: no se ha corrido (gasta cuota).
- [x] Repo movido a `workshops/03-datos-abiertos-mcp/claude-mcp-ibero-2026`; `verificar.py 4` sigue en verde desde ahí.
- [ ] Volver a abrir `claude` desde la nueva ruta: preguntará de nuevo por confianza y por activar `cdmx` (la marca de "desactivado" era solo de la ruta vieja).
