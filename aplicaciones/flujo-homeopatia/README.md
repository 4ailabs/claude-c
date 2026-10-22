# Cómo correr el flujo de homeopatía

Nota práctica para analizar una consulta con el flujo nuevo: **el modelo propone, el código verifica y el doctor decide.**

- El diseño completo está en [`../sistema-consulta-homeopatia.md`](../sistema-consulta-homeopatia.md).
- El diagrama está en [`../flujo-homeopatia.html`](../flujo-homeopatia.html), publicado en https://claude.ai/artifact/JBTEq54RGjPnSYD4kEfeFL.

> **Regla de privacidad:** este repo (`claude-c`) no lleva datos de pacientes. Los casos reales se trabajan en la carpeta del sistema de consulta de la Mac, y lo que se genere se queda ahí. El ejemplo de `ejemplo/` es ficticio.

## Qué hay en esta carpeta

| Archivo | Para qué |
|---|---|
| `validar_caso.py` | El control en código de F1 y F3: verifica cada cita contra la transcripción y aplica la Regla de los Tres. Solo usa Python, sin dependencias ni modelos. |
| `ejemplo/transcripcion.json` | Transcripción ficticia en el formato de Voxtral. |
| `ejemplo/caso.json` | El caso depurado de ese ejemplo: el formato que debe producir el paso 2. |
| `ejemplo/afirmaciones.json` | Opcional: datos de un análisis previo para comprobar si están en la grabación. |

Pruébalo con el ejemplo:

```bash
python3 validar_caso.py ejemplo/caso.json ejemplo/transcripcion.json ejemplo/afirmaciones.json
```

Sale con código `0` si ya se pueden nombrar candidatos y `1` si hay que pedir más datos.

## El proceso, paso a paso

### 0. Abrir Claude en la Mac

Los expedientes y las transcripciones solo están en la Mac, así que la sesión tiene que correr ahí. Una sesión de Claude en la nube solo ve lo que está subido a GitHub.

```bash
cd ~/Sistema-consulta          # la carpeta del sistema de consulta
claude                         # o `claude remote-control` para manejarla desde la app
```

Ten también este repo clonado, por ejemplo en `~/claude-c`, y actualizado con `git pull`.

### 1. Encontrar la transcripción

El watcher deja cada consulta en `transcripciones-entrantes/` como un JSON de Voxtral con hablantes separados. **Ese archivo no se edita nunca**: es el original contra el que se verifica todo.

### 2. Depurar síntomas (F1) → `caso.json`

Pídeselo a Claude con este mensaje, cambiando la ruta de la transcripción:

```text
Depura la consulta de transcripciones-entrantes/<archivo>.json siguiendo
~/claude-c/aplicaciones/flujo-homeopatia/README.md (paso 2).
Usa solo esa transcripción: nada de consultas anteriores ni de otros pacientes.
Guarda el resultado como caso.json en la carpeta del paciente, con el formato de
~/claude-c/aplicaciones/flujo-homeopatia/ejemplo/caso.json.
```

Reglas para cada síntoma de `caso.json`:

- `cita`: **la frase literal** del paciente, copiada tal cual de la transcripción. Una frase corta basta.
- `t`: el minuto donde aparece.
- `clase`, según la Fase 1 del protocolo de repertorización:
  - `repertorizable`: lo dijo el paciente en esta consulta y tiene modalidad, localización o concomitante, o es raro y peculiar.
  - `informativo`: común a la enfermedad, sin modalidad, o un antecedente.
  - `excluir`: posible efecto de un medicamento, o un dato de otra consulta.
- `nivel`: del 1 al 5, según la jerarquía de Kent del protocolo.
- `medicamentos`: todo lo que tome el paciente, porque decide qué se excluye.

Si un dato viene de lo que el paciente dijo **después** de la grabación (por chat o en persona), se anota con `"t": "fuera de grabación"` y con la fuente en `motivo`. El validador lo va a marcar `SIN CITA`, y eso es lo correcto: un dato sin fuente no debe decidir el remedio.

### 3. Verificar el caso (control en código)

```bash
python3 ~/claude-c/aplicaciones/flujo-homeopatia/validar_caso.py \
  pacientes/AAAA/MM/Nombre/caso.json \
  transcripciones-entrantes/<archivo>.json
```

- Cada síntoma `SIN CITA` que estaba como repertorizable baja a informativo.
- Si la Regla de los Tres no se cumple (✘), el resultado es **🔴 pedir más datos**: se vuelve a preguntar al paciente y no se nombra ningún remedio.

### 4. Repertorizar (F2)

Con los síntomas ✅ que pasaron la verificación, el modelo propone las rúbricas a buscar y se elimina por filtro, como dice el protocolo: no por suma.

> **Pendiente:** todavía no hay un repertorio cargado. Hasta que lo haya (Kent local en SQLite u OOREP, una decisión del doctor), esta fase depende del conocimiento del modelo y hay que decirlo en el análisis.

### 5. Diferencial (F3)

Pídele a Claude que ataque al candidato **en una conversación nueva o con un subagente** que reciba solo `caso.json` y el nombre del candidato, sin el razonamiento anterior. Debe:

- encontrar el síntoma que separa al candidato de sus dos diferenciales más cercanos;
- aplicar la tabla anti-sesgo de policrestos del protocolo;
- entregar el semáforo 🟢 🟡 🔴 con su razón.

### 6. El doctor decide (F4)

Se le presenta una tabla con el candidato y los diferenciales, los síntomas a favor y en contra (cada uno con su cita y minuto), el semáforo y las preguntas para la próxima consulta. Nada se guarda sin su aprobación.

### 7. Guardar (F5)

Como hoy: el `.md` en la carpeta del paciente y la receta por `save_prescription_to_panel.cjs`. **No usar SQL libre.** La receta lleva solo producto, dosis y forma de toma.

## Comparar con un análisis anterior (opcional)

Para revisar un análisis ya hecho, lista en un `afirmaciones.json` los datos en que se apoyó, cada uno con un patrón de búsqueda, y pásalo como tercer argumento:

```bash
python3 validar_caso.py caso.json transcripcion.json afirmaciones.json
```

El reporte dice qué datos aparecen en la grabación y cuáles no. Así se probó el flujo con la consulta de Paciente X del 29 de julio: 7 de los datos del análisis, incluido el que desempató el remedio, no estaban en la grabación. Ese caso no se subió a este repo.

## Qué falta

| Pieza | Estado |
|---|---|
| F1 `caso.json` + `validar_caso.py` | ✅ Funciona; probado con un caso real y uno negativo |
| Regla de los Tres en código | ✅ Funciona |
| F2 con repertorio real | ⏳ Falta elegir y cargar el repertorio |
| F3 en contexto separado | ⏳ Manual (conversación nueva); falta el subagente |
| F5 `guardar_receta` con esquema cerrado | ⏳ Falta; corregir `next_appointment` en el script actual |
| F6 evals | ⏳ Falta armar los casos anonimizados y los pares |
| Decisiones del doctor | ⏳ Mental o físico primero · bloquear o 🟡 · qué repertorio |
