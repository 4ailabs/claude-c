# Notas · Del agente al equipo

**Ponente:** Jésica Tapia (NLP & AI Policy Specialist, UNESCO, según el programa; en el audio se presenta con más detalle, ver Dudas) · **Fuente:** `transcripts/05-del-agente-al-equipo/sesion.md` (grabación `20261019 1959`, 49.5 min, 19:59–20:48).
**Alcance:** los primeros ~9 minutos de la grabación son el **cierre del workshop 4** (un video del enjambre y el concurso de las placas); su ponencia empieza hacia `[00:09:54]`.
**Repo:** el de evaluación multiagente de la ponente (en su GitHub; el nombre exacto no se oye y no se ha clonado).

> Convención: `[hh:mm:ss]` = marca de la transcripción. **(?)** = dudoso por la transcripción automática (nombres, cifras, términos técnicos). Nada está corregido de memoria.

## Temas en el orden en que se dieron

### 0. Cierre del workshop 4 y transición `[00:00:00–00:09:21]`
- Video del enjambre (ver `workshops/04-physical-ai-mcp-swarm/notas.md`, apéndice) `[00:00:19–00:03:50]`.
- Concurso de las placas por seguidores de LinkedIn en cada mesa `[00:04:48–00:08:41]`; aplauso a Jonathan Olvera `[00:08:42]`.
- Se anuncia la "última práctica de la noche", una **foto grupal antes de las nueve** y una sorpresa `[00:09:25–00:09:50]`.

### 1. Quién es y por qué le importa `[00:09:54–00:16:02]`
- Viene de las **ciencias sociales**; aprendió a programar desde joven, así que pasar a la IA le fue fácil `[00:10:16–00:10:38]`.
- Trabaja en adopción y transformación digital de pymes (en el audio, "GTO de Analítica Boutique" (?)) `[00:10:48–00:10:58]`; hace **auditoría de políticas** y de propuestas de regulación, para pasarlas a los equipos de desarrollo y que "no se queden en un buen deseo" `[00:11:31–00:12:06]`.
- **IA ética técnica:** no son solo valores; implica **evaluaciones** y observar el comportamiento no solo de la tecnología sino de "los agentes adaptativos que somos los humanos y las organizaciones" `[00:12:10–00:12:51]`.
- Experiencia: sistemas para comunidades vulnerables, perspectiva de género, bases de datos con sesgos, **arquitecturas multiagente seguras para la niñez** `[00:13:07–00:14:24]`. Da clases en universidades (UNAM y otra (?)) `[00:14:24–00:14:36]`. Es **embajadora de la comunidad de Claude en México** `[00:15:39]`.

### 2. El caso del taller: auditar un sistema de selección de CVs `[00:16:20–00:18:52]`
- Empresas le piden auditar si usan bien un sistema que evalúa **CVs**, tras una queja `[00:16:23–00:16:46]`. En Latinoamérica hay "mucha charlatanería" y sistemas no ajustados a la realidad `[00:16:53–00:17:08]`.
- **El sesgo no viene solo de los datos:** también de los hábitos de las personas. Ejemplo: pedir "mayor disponibilidad de tiempo" para un puesto de jornadas largas descarta, sin decirlo, a quien tiene otras obligaciones `[00:17:17–00:18:09]`.
- La auditoría coloca **barandillas (guardrails) a la entrada y a la salida** para ver cómo se procesa la información del operador y cómo el agente coordinador la pasa `[00:18:30–00:18:55]`.

### 3. Diseño del sistema multiagente `[00:19:00–00:20:46]`
- **Tres especialistas**, cada uno con un modelo distinto: "a veces no necesitas toda la potencia para todo" `[00:19:00–00:19:16]`.
- "Los sistemas de agentes **no son para todo**": a veces se gastan muchísimos tokens sin necesidad `[00:19:21–00:19:37]`.
- **Por diseño, el orquestador no comparte toda la conversación** con los otros agentes `[00:19:37–00:19:52]`. Al **compactar** el contexto, si no está bien hecho, se pueden perder las barandillas `[00:20:01–00:20:21]`. Si el orquestador se equivoca al pasar el contexto, hay **errores en cascada** que nadie nota `[00:20:21–00:20:43]`.

### 4. Pasos del repositorio y regulación `[00:20:46–00:26:38]`
1. Crear el sistema; 2. procesar un CV de ejemplo "con cierta maña para que levante problemas"; 3. las barandillas y una **rúbrica**; 4. una evaluación `[00:20:58–00:21:30]`.
- **Regulación:** el AI Act de la Unión Europea apunta a usos como educación y salud, y exige **bitácoras**; menciona diciembre de 2027 para la regulación fuerte (?) `[00:21:40–00:22:02]`.
- Las bitácoras llevan **hash**: "la tentación de modificar las bitácoras cuando algo funciona mal es mucha"; la regulación pide registrar cualquier modificación `[00:22:06–00:22:31]`.
- **Sin créditos:** hay un **modo simulación** que recorre los pasos; con API key hace las llamadas, y avisa un cálculo aproximado de llamadas para no gastar el crédito `[00:22:44–00:23:40]`. Hay versión en inglés y se puede seguir "con código a mano o con Claude" `[00:23:52–00:24:02]`.
- **Dashboards:** para auditar en producción salen demasiadas cosas; hacen falta interfaces distintas para cada público (legal, no técnicos) `[00:25:07–00:25:44]`. Prefiere **definir todos los agentes en un solo lugar** para poder encontrar las barandillas `[00:25:57–00:26:38]`.

### 5. Demostración `[00:27:45–00:43:30]`
- Se corre el taller con Claude Code: `verificar`, abre el dashboard y crea el sistema `[00:27:49–00:28:41]`.
- **Barandillas del sistema:** **nunca recomienda a quién contratar**; eso se reserva a las personas `[00:29:14–00:29:27]`, por el **sesgo de automatización** (si el sistema recomienda, no se cuestiona), que ya está contemplado en la ley europea `[00:29:33–00:30:22]`.
- **Tres especialistas** `[00:30:27–00:31:42]`: (1) compara cada requisito con el CV y **no inventa** nada que no esté ahí; (2) revisa lo "contradictorio" sin **penalizar pausas laborales** ni especular (hay estudios donde se castiga más a las mujeres por esas pausas); (3) consistencia de fechas y cargos, y formula dudas para la entrevista.
- "**Lo que no dice, el LLM lo va a inventar** a menos que se lo prohíbas explícitamente" `[00:32:05–00:32:26]`.
- El orquestador **puede decidir no consultar a los especialistas** si cree que ya sabe; parte de la auditoría es verificar **qué herramientas llamó** `[00:32:26–00:33:23]`. Los especialistas están como herramientas de una lista y no comparten contexto `[00:33:23–00:33:49]`.
- **Caso de prueba:** una candidata de 38 años, casada; la salida **ingenua** la penaliza por ser madre de familia y por la pausa laboral `[00:34:20–00:34:50]`. El CV trae además una **instrucción oculta** para el LLM (inyección de prompt de un candidato); las personas ya ponen instrucciones a los sistemas de RH `[00:36:01–00:36:56]`. La corrida ingenua **recomienda contratar** y expone datos personales `[00:37:05–00:38:19]`.
- **Corrida protegida** `[00:40:36–00:43:10]`: no recomienda, entrega un puntaje con razones, no menciona atributos protegidos, **ignora la instrucción oculta** y no penaliza las pausas. Las **trazas** quedan con hash; si se modifica un caso, el hash lo detecta `[00:43:18–00:43:50]`.

### 6. Tensiones y lecciones `[00:37:27–00:46:39]`
- **Bitácora vs privacidad:** hay que guardar todo, pero hay datos personales; "todavía no está muy bien resuelto en las leyes". Ella audita como tercera y no debería saber quién es cada persona `[00:37:27–00:38:09]`.
- **Métricas y alertas:** las alertas no las verá ingeniería sino RH; es un reto `[00:38:29–00:38:51]`. Miles de CVs al día necesitan control humano de la auditoría `[00:38:51–00:39:13]`.
- **Costo:** los sistemas multiagente son más verbosos y caros; solo valen si el problema lo paga `[00:39:28–00:39:57]`. **Evaluar también cuesta**, y con barandillas la cuenta sube `[00:40:18–00:40:31]`.
- **Atributos protegidos** (género y otros): los clasificadores de IA predictiva traen sus sesgos al contexto del LLM; las barandillas deben protegerlos aunque vengan de un resultado matemático `[00:41:18–00:42:32]`.
- **Confianza:** tras la evaluación, la gente confía de otra forma en el sistema; "no todo es alto riesgo" y hay que comunicar hasta dónde es seguro `[00:44:58–00:45:53]`.
- **Huella de carbono:** se puede restringir qué modelos se usan y medirlo `[00:46:03–00:46:39]`.

### 7. Ejercicios que deja `[00:46:39–00:49:10]`
- Cambiar atributos e **idiomas** y ver qué pasa `[00:47:59]`.
- Agregar una **señal indirecta** (p. ej. universidad pública frente a privada) `[00:48:12]`.
- **Sesgo de género con pares:** dos CVs idénticos que solo cambian hombre/mujer; si el resultado cambia, hay sesgo `[00:48:21–00:48:44]`.

## Dudas abiertas
- Cómo se presenta exactamente (empresa, cargo e institución en Washington): la transcripción es confusa `[00:10:48–00:11:49]`; el programa dice UNESCO.
- Nombre del repositorio y de la guía (solo se oye "repositorio de evaluación multiagente").
- La fecha "diciembre de 2027" para la regulación `[00:21:40]`.
- Qué frase exacta dice la instrucción oculta del CV `[00:36:42]`.
