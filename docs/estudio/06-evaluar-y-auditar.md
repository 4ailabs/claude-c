# Módulo 6 · Evaluar, auditar y responder por un sistema

**Tiempo:** unas 2.5 horas · **Prerrequisitos:** módulos 1 a 5 · **Clase principal:** workshop 5 (Jésica Tapia) · **También:** W1, W3

## Al terminar podrás

- Distinguir una **evaluación de elección de tools** de una **auditoría de sesgo**.
- Hacer una prueba con **pares de casos idénticos** y leer el resultado.
- Explicar qué es una bitácora con hash y qué tensión tiene con la privacidad.
- Decidir cuándo un sistema multiagente **no** vale la pena.

## 1. La idea en simple

Probar que un sistema "funciona" no basta: hay que probar **que no hace daño** y poder **demostrarlo**. Es la diferencia entre decir "creo que el puente aguanta" y mostrar el informe de carga, firmado y sin enmendaduras.

## 2. Cómo funciona

**Dos tipos de evaluación:**

| | Pregunta | Ejemplo |
|---|---|---|
| **De elección** | ¿El modelo usa la tool y los argumentos correctos? | 10 preguntas con la tool esperada; incluye casos negativos («¿cuál es la capital de Francia?» no debe usar la tool) `W3 [00:30:03–00:30:57]` |
| **De sesgo y cumplimiento** | ¿El sistema trata igual a casos iguales y respeta la ley? | Pares de CVs idénticos que solo cambian hombre/mujer `W5 [00:48:21–00:48:44]` |

**Cómo se audita un sistema de selección de CVs** `W5`:
1. El sesgo **no viene solo de los datos**, también de los hábitos humanos: pedir "mucha disponibilidad" excluye, sin decirlo, a quien tiene otras obligaciones `[00:17:17–00:18:09]`.
2. Se compara una corrida **ingenua** con una **protegida** `[00:34:20–00:43:10]`.
3. Lo que se vigila: que no se mencionen **atributos protegidos** (ni siquiera los que vengan de un modelo predictivo ya sesgado) `[00:41:18–00:42:32]`; que el orquestador **sí consulte** a los especialistas (se revisa qué herramientas llamó) `[00:32:26–00:33:23]`; y que "lo que no dice, el LLM lo inventa" a menos que se prohíba `[00:32:05]`.
4. Se prueban ejercicios: pares de CVs, otros idiomas y una señal indirecta (universidad pública o privada) `[00:46:39–00:48:44]`.

**Regulación y bitácoras** `W5 [00:21:40–00:22:31]`: el AI Act de la Unión Europea apunta a usos como educación y salud y exige **bitácoras**. Llevan **hash** para detectar modificaciones: "la tentación de modificarlas cuando algo falla es mucha".
**Tensión sin resolver:** hay que guardarlo todo, pero hay datos personales; "no está bien resuelto en las leyes" `[00:37:27–00:38:09]`.

## 3. Lo que dijeron en las clases

- **W5:** el sistema **nunca recomienda a quién contratar**, por el *sesgo de automatización*: si el sistema lo recomienda, la persona no lo cuestiona `[00:29:14–00:30:22]`.
- **W5:** los sistemas multiagente son más verbosos y caros, "no son para todo", y **evaluar también cuesta** `[00:19:21–00:19:37]` · `[00:39:28–00:40:31]`. Tras la evaluación la gente confía de otra forma en el sistema `[00:44:58–00:45:39]`.
- **W3:** si una tool falla, se corrige su descripción y su esquema, no el prompt; evaluar es un trabajo iterativo `[00:38:03–00:38:33]`.
- **W1:** el taller termina midiendo la tasa de error de herramientas de tu agente, por categoría y con costo.

## 4. Pruébalo tú

**Sin gastar nada:**

```bash
python3 docs/estudio/ejercicios/06_par_de_cvs.py
```

Dos CVs idénticos salvo la pausa laboral reciben 145 y 130: **esa diferencia es sesgo**. Con la barandilla (el atributo no entra al puntaje) la diferencia es 0. Añade tú otra variable "proxy" (p. ej. `estado_civil`) y repite la prueba.

**Con el repo del W5** (cuando tengas el enlace): corre primero en **modo simulación**, que no gasta créditos.

## 5. Errores comunes

- Evaluar solo "si funciona" y no si trata igual a casos iguales.
- Creer que quitar la columna `genero` basta: otras variables (*proxies*) lo filtran.
- Una bitácora que se puede editar sin dejar rastro.
- Alertas que solo verá ingeniería cuando quien debe actuar es otra área.
- Adoptar un sistema multiagente cuando uno solo bastaba.

## 6. Preguntas de repaso

1. ¿Qué mide una prueba con pares de casos idénticos?
2. ¿Qué es el sesgo de automatización y cómo lo evita el diseño del sistema?
3. ¿Para qué sirve el hash en una bitácora?
4. ¿Cuándo no conviene un sistema multiagente?

<details><summary>Respuestas</summary>

1. Si dos casos iguales reciben resultados distintos; la diferencia es un sesgo del sistema.
2. Es no cuestionar lo que recomienda un sistema; se evita haciendo que el sistema **no recomiende**, y deje la decisión a la persona.
3. Para detectar si alguien modificó una entrada pasada: la cadena de hashes deja de coincidir.
4. Cuando el problema no paga el costo extra (más tokens, más verboso) o un agente solo lo resolvería.
</details>

## 7. Conecta con

- Anterior: [Módulo 5](05-mundo-fisico-y-enjambres.md). Vuelve al [Módulo 1](01-el-agente-actua.md) para medir tasas de error.
- Conceptos 16, 17, 22 y 23 de [conceptos.md](../conceptos.md).
