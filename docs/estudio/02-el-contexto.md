# Módulo 2 · El contexto: cómo se llena, se degrada y se compacta

**Tiempo:** unas 2 horas · **Prerrequisitos:** módulo 1 · **Clase principal:** workshop 2 (Alejandro Martínez) · **También:** W3, W5

## Al terminar podrás

- Decir de qué se compone el contexto y por qué se degrada (*context rot*).
- Explicar la diferencia entre compactar **sin** y **con** referencia.
- Describir el disco como memoria (`search_file`, `read_file`, `write_file`).
- Decidir, con criterio, cuándo **no** compactar.

## 1. La idea en simple

El contexto es **la mesa de trabajo del modelo**: solo lo que está sobre la mesa existe para él. Es finita, y cuanto más llena, peor encuentra las cosas. Compactar es **guardar los papeles viejos en un archivero** y dejar sobre la mesa una nota que dice dónde están.

## 2. Cómo funciona

**El contexto se compone de:** instrucciones, **definiciones de tools**, el chat actual, resúmenes y el contexto buscado (documentos, búsquedas, respuestas de otros agentes) `W2 [00:03:39–00:04:27]`.

**Context rot.** Los anuncios hablan de 1 millón de tokens, pero la calidad baja desde unos ~128 mil según el benchmark que citó el ponente `[00:05:05–00:06:21]`. En vivo, con 130–200 mil tokens, Haiku contestó "no puedo responder" aunque el dato estaba, y a veces respondió seguro pero mal `[00:11:28–00:12:42]`.

**Compactar:**

| | Qué queda en el contexto | Qué se pierde |
|---|---|---|
| **Sin referencia** | Solo el resumen | Los detalles que el resumen no recogió |
| **Con referencia** | El resumen + una **ruta al original** guardado | Casi nada: el agente puede buscarlo |

**El disco como memoria** `[00:16:17–00:17:49]`:
- `search_file`: como `grep`, devuelve solo las líneas con el texto buscado y su número.
- `read_file`: lee un rango de líneas (por ejemplo, de la 100 a la 200).
- `write_file`: guarda texto en un archivo.

Lo que devuelve una tool **entra completo al contexto**, así que se busca primero y se lee solo lo necesario. En la demo, el contexto bajó de unos 130,000 a unos 5,000 tokens (cifra a confirmar) y el agente igual encontró el dato `[00:21:03–00:21:35]`.

## 3. Lo que dijeron en la clase (W2)

- "Para un LLM, **un puntero es texto plano**" `[00:19:41]`; "no todo tiene que estar fresco todo el tiempo en la mente del agente" `[00:21:35]`.
- Otras técnicas: truncar (los 100 mensajes más recientes de 1,000), limpiar resultados de tools, compresión por tokens, notas, subagentes, y resumen total, parcial o estructurado `[00:21:52–00:24:50]`.
- El resumen **estructurado** no lo recomienda: el siguiente modelo "va a deshacer cualquier implementación a la medida". Prefiere la compactación con referencia, que "ha sobrevivido varios modelos" `[00:24:20–00:24:50]`.
- **Subagentes:** en vez de cargar todo, un agente por cliente con su parte y un orquestador. El contexto se vuelve dinámico y auditable `[00:25:18–00:28:12]`.
- **Cuándo no:** implementar estos mecanismos puede romper la **caché** y subir costos; "hay que saber cuándo compactar", y el umbral depende del sistema `[00:29:53–00:30:59]`.
- **W5:** el orquestador **no comparte toda la conversación** por diseño; si el contexto se compacta mal se pierden las barandillas, y un error al pasar contexto produce **errores en cascada** `[00:19:37–00:20:43]`.

## 4. Pruébalo tú

**Sin gastar nada:**

```bash
python3 docs/estudio/ejercicios/02_compactar_con_referencia.py
```

Verás un historial de 14,179 caracteres con un serial escondido: el resumen **sin** referencia lo pierde; el que lleva referencia no lo tiene a la vista pero **lo recupera buscando** en el archivo con una fracción del costo.

**Con el repo** (`workshops/02-context-engineering/context-engineering-workshop`): abre `paso2_disco.py` (ya escrito) y compáralo con `paso3_compactacion.py` de la rama `solucion`. Con una API key con créditos, levanta la app, carga la "conversación muy larga" y compara las barras de contexto antes y después.

## 5. Errores comunes

- Creer que más ventana significa mejor respuesta.
- Compactar **sin** dejar un puntero al original.
- Devolver un archivo entero en vez de buscar y leer un rango.
- Compactar sin medir: puede romper la caché y encarecer.

## 6. Preguntas de repaso

1. ¿Qué cosas ocupan contexto además del chat?
2. ¿En qué se diferencia compactar sin y con referencia?
3. ¿Por qué se busca primero y se lee después un rango?
4. Da dos razones para **no** compactar siempre.

<details><summary>Respuestas</summary>

1. Instrucciones, definiciones de tools, resúmenes y el contexto buscado.
2. Con referencia se guarda el original y el resumen lleva su ruta, así se pueden recuperar detalles sin recargarlo todo.
3. Porque lo que devuelve una tool entra completo al contexto; un archivo grande volvería a llenar la ventana.
4. Puede romper la caché y subir costos, y un resumen mal hecho pierde detalles (o las barandillas).
</details>

## 7. Conecta con

- Anterior: [Módulo 1](01-el-agente-actua.md). Siguiente: [Módulo 3 · MCP](03-mcp-y-diseno-de-tools.md), donde las definiciones de tools son lo que más pesa.
- Subagentes y barandillas: [Módulo 4](04-controles-y-seguridad.md).
- Conceptos 5 a 9 de [conceptos.md](../conceptos.md).
