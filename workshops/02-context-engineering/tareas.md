# Tareas y ejercicios

Código en el repo del ponente: `workshops/02-context-engineering/context-engineering-workshop` (https://github.com/alexMtzRivero/context-engineering-workshop).
Aquí queda la consigna, el plan y el avance.

## Consigna

No hubo una entrega formal. Lo que pidió el ponente en la sesión:

1. Clonar el repo y **usar la rama `solucion`**, porque el tiempo no alcanza para escribir todo `[00:08:26]`.
2. Cargar la **conversación muy larga** y hacer la pregunta rápida «¿cuál de los cinco clientes recibe su reposición primero?» con Haiku `[00:10:03–00:11:28]`.
3. Probar **compactar sin referencia** y **con referencia**, y comparar qué conserva cada una `[00:14:52–00:21:35]`.
4. Probar **un agente por cliente** (subagentes) `[00:25:18–00:29:34]`.
5. Opcional: **mejorar lo que ya está implementado**, p. ej. el prompt del resumen, que él mismo llama mediocre `[00:08:33, 00:13:53]`.

En el README del repo, los pasos para escribir el código son: paso 2 (`paso2_disco.py`), paso 3 (`paso3_compactacion.py`), paso 4 (`paso4_descubrimiento.py`) y paso 5 extra (`paso5_subagente.py`). El paso 4 no se cubrió en la sesión.

## Plan

1. Paso 2: funciones de disco (`list_files`, `read_file`, `search_file`, `write_file`).
2. Paso 3: `compact` con y sin referencia.
3. Ver la app corriendo y comparar la barra de contexto antes y después de compactar.
4. Opcional: paso 5 (subagentes) y paso 4.

## Avance

- [x] Repo clonado y entorno listo en `.venv` (Python 3.14); 17 de 27 pruebas pasan, las 10 restantes son de los pasos 3, 4 y 5.
- [x] **Paso 2 escrito** en `paso2_disco.py`, sin commitear en `main` del repo del ponente.
- [x] App levantada en `http://127.0.0.1:8000` (carga bien; luego se detuvo).
- [x] Leída la solución oficial del paso 3 (rama `solucion`) y explicada.
- [ ] Paso 3 propio (`compact`): pendiente.
- [ ] **Falta una llave de Anthropic con créditos** en `.env` (`MODEL=anthropic:claude-haiku-5-5`, `ANTHROPIC_API_KEY=...`). Sin ella el chat no responde; la conversación larga sí carga sin API. La llave de `Obesidad` respondió "credit balance too low".
- [ ] Pasos 4 y 5: pendientes.
