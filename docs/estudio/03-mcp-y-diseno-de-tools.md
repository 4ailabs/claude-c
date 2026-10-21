# Módulo 3 · MCP y el diseño de tools

**Tiempo:** unas 2.5 horas · **Prerrequisitos:** módulos 1 y 2 · **Clase principal:** workshop 3 (Dante Bazaldua) · **Material:** `datos-mcp-ibero.pdf`

## Al terminar podrás

- Explicar qué es MCP y sus tres actores y tres piezas.
- Elegir entre **MCP, CLI y API**, con sus costos.
- Diseñar una tool para que el modelo la elija bien.
- Saber qué es una skill y cuándo conviene.

## 1. La idea en simple

Sin un estándar, cada app de IA necesita una integración distinta con cada sistema. **MCP es como un enchufe universal**: cada app implementa el cliente una vez, cada sistema su servidor una vez, y todo se conecta. Con 3 apps y 4 sistemas son 3 + 4 = 7 piezas, no 3 × 4 = 12 integraciones (según el PDF).

## 2. Cómo funciona

- **Tres actores:** el **host** (Claude Code), el **cliente** (el conector que el host crea) y el **servidor** (tu código, aquí en Python con FastMCP) `W3 [00:14:03–00:14:39]`.
- **Qué ofrece un servidor:** *tools* (decide el modelo), *resources* (datos de solo lectura, los decide la app) y *prompts* (plantillas que tú eliges ejecutar) `[00:15:47–00:16:12]`.
- **Transporte:** HTTP local (el del taller), `stdio` (el host lanza tu programa) o remoto con OAuth `[00:16:26–00:16:55]`.
- En el taller el servidor corre en `127.0.0.1:8765`, y `.mcp.json` le dice a Claude Code dónde está.

**MCP, CLI o API** `W3 [00:10:17–00:14:03]`:

| | Conviene si… | Costo |
|---|---|---|
| **API** | el flujo es siempre el mismo y no decide un modelo (script, pipeline) | Cada servicio se documenta distinto |
| **CLI** | trabajas en tu máquina con herramientas que el modelo ya conoce (git, gh) | Corre con todos tus permisos; sin terminal no hay CLI |
| **MCP** | el modelo decide en el momento, para varias personas, con permisos y auditoría | Las definiciones ocupan **contexto**; cada paso pasa por el modelo; es otro servicio que operar |

Según el PDF, el MCP de GitHub tiene 93 tools y ocupa unos 55,000 tokens solo en definiciones.

## 3. Diseñar tools para un agente (W3)

- "Un API es un contrato, ¿quién lo lee? Los **modelos**" `[00:22:52]`.
- **Por intención, no por endpoint.** No expongas `ejecutar_sql`; ofrece `afluencia_metro(estación, línea, desde, hasta)` `[00:23:06–00:23:26]`.
- **Errores que corrigen.** Si «insurgente» coincide con varias estaciones, el error ofrece las opciones `[00:23:29–00:23:41]`.
- **Respuestas cortas** y argumentos planos `[00:37:10–00:37:49]`; el contexto no debe explotar.
- **Criterios de calidad (TDQS):** propósito, cuándo usarla, comportamiento, parámetros, concisión y completitud `[00:37:53]`.
- **El docstring es la descripción que lee el modelo** `[00:22:45]`.

**Skills y plugins:** una skill enseña al agente a usar bien la herramienta; un plugin junta el MCP y la skill, y es un buen patrón para distribuir `[00:28:53–00:29:36]`.

## 4. Pruébalo tú

**Sin gastar nada:**

```bash
python3 docs/estudio/ejercicios/03_tool_bien_disenada.py
```

Compara una tool `ejecutar_sql` (el error no enseña nada) con `afluencia_metro` (los errores dicen qué hacer).

**Con el repo** (`workshops/03-datos-abiertos-mcp/claude-mcp-ibero-2026`): `uv run servidor.py`, abre `claude` en la carpeta, activa `cdmx` en `/mcp` y pregunta «¿Cuánta gente entró a Pantitlán en julio de 2026?» (4,623,233). Luego pregunta por «insurgente» mal escrito y observa el error que corrige.

## 5. Errores comunes

- Exponer una tool genérica (SQL libre) "para que el modelo decida".
- Errores del tipo "algo falló", que no dicen qué corregir.
- Devolver miles de filas en vez de un agregado.
- Conectar muchos MCP sin medir lo que pesan sus definiciones.
- Usar MCP donde bastaba un script o una CLI.

## 6. Preguntas de repaso

1. ¿Qué diferencia hay entre una *tool*, un *resource* y un *prompt* en MCP?
2. ¿Cuándo preferirías una CLI a un MCP?
3. Menciona dos costos de usar MCP.
4. Reescribe «ejecutar SQL» como una tool mejor diseñada.

<details><summary>Respuestas</summary>

1. Tool: la invoca el modelo. Resource: un dato de solo lectura que decide la app. Prompt: una plantilla que tú ejecutas.
2. Cuando trabajas en tu máquina con una herramienta que el modelo ya conoce y no necesitas permisos por persona ni auditoría.
3. Tokens por las definiciones, y que cada paso pasa por el modelo; además, otro servicio que desplegar y probar, y riesgos de seguridad.
4. Por ejemplo `afluencia_metro(estacion, linea, desde, hasta)`: una intención clara, con errores que ofrecen opciones.
</details>

## 7. Conecta con

- Anterior: [Módulo 2](02-el-contexto.md). Siguiente: [Módulo 4 · Controles y seguridad](04-controles-y-seguridad.md).
- Evaluar si el modelo elige bien: [Módulo 6](06-evaluar-y-auditar.md).
- Conceptos 10 a 12 y 15 de [conceptos.md](../conceptos.md).
