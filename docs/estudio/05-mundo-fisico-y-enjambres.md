# Módulo 5 · Del agente al mundo físico y al enjambre

**Tiempo:** unas 1.5 horas · **Prerrequisitos:** módulos 1 a 4 · **Clase principal:** workshop 4 (Jonathan Olvera) · **También:** W5 (video de cierre)

## Al terminar podrás

- Explicar por qué una placa "ve pero no piensa" y dónde ocurre el razonamiento.
- Definir umbrales y frecuencias según el riesgo, y cuándo llamar a un humano.
- Describir qué cambia cuando los agentes interactúan con agentes de otras personas.
- Explicar cómo una "vacuna" protege a una red sin compartir datos.

## 1. La idea en simple

Hasta ahora, un error se arregla borrando y repitiendo. Con una **válvula** o una puerta, no. Un agente que toca el mundo físico es como **un guardia de seguridad con un radio**: ve algo, pregunta a su central y, si hay dos señales de peligro, **llama a una persona** antes de actuar.

## 2. Cómo funciona

**Physical AI en el taller** `W4`:
- Una placa **ESP32 con cámara** toma una foto **cuando cambia la escena** `[00:28:19–00:28:24]`.
- "Una placa **ve, pero no piensa**" `[00:11:00]`: hay modelos pequeños que correrían en la placa, "pero no son tan inteligentes", así que la foto se manda a **Claude**, que la describe en un flow de Hiveflow `[00:10:19–00:10:28]` · `[00:31:19–00:32:01]`.
- El flow evalúa riesgo (un derrame, fuego) y lo manda a un **enjambre** que junta lo que ven varias cámaras; si hay alerta, manda un correo (o WhatsApp, Telegram, Slack) `[00:32:52–00:33:12]`.

**Controles para lo físico** `[00:17:25–00:18:23]`:
- Definir las **consecuencias**: qué valores son "rojos".
- Definir **frecuencia y alcance**: si hay riesgo de fuego, quizá cada segundo; una fuga de agua poco riesgosa, cada minuto.
- Un **humano** confirma, y se lleva una **bitácora**.

**Enjambres** `[00:04:37–00:05:43]`: "la siguiente ola" es que **los agentes interactúen con agentes de otras personas**. Eso exige protocolos de **seguridad y comunicación**.
- Caso real: un proyecto público de tableros para agentes (SwarmMind (?), `swarmind.sh`) recibió unos **3,000 agentes** en la primera semana. Para pedirle cuentas a uno, **un correo por agente** `[00:19:45–00:20:35]`.
- **Simulación:** el enjambre espera varias señales; con **dos o tres criterios** apuntando a una emergencia, pide permiso a una persona `[00:20:46–00:21:33]`.
- **Vacunas:** si un nodo "se infecta", aprende y **comparte el patrón**, no los datos `[00:21:33–00:22:45]`.

**El video de cierre** (grabado al inicio del W5): hospitales que no comparten datos pero sí cómo es una estafa. Con federación, **0 engañados** frente a **12** si cada hospital atendiera solo (cifras del video, no verificadas) `W5 [00:02:45–00:03:50]`.

## 3. Lo que dijeron en la clase

- "Cuando pones un MCP y muchas de estas herramientas, la responsabilidad cae en ti como programador o ingeniero" `[00:09:40]`.
- **El modelo puede equivocarse**; hacen falta filtros y humano en el loop `[00:34:20–00:34:51]`.
- Riesgo de la **caja negra:** hay que poder mostrar a un compañero no técnico dónde se atoró un flujo; buscan "lo mejor de los dos mundos", lo agéntico y lo visual `[00:35:18–00:36:21]`.
- Idea para casa: conectar la placa a la computadora y pedirle a Claude cómo leer los sensores; se pueden construir **MCP alrededor de la placa** `[00:15:01–00:16:46]`.

## 4. Pruébalo tú

**Sin gastar nada:**

```bash
python3 docs/estudio/ejercicios/05_umbral_y_bitacora.py
```

Una señal no escala; dos sí. La bitácora lleva un **hash encadenado**: edita una entrada y la verificación falla. Cambia `CRITERIOS_EMERGENCIA` a 1 o a 3 y observa el equilibrio entre falsas alarmas y reacción tardía.

**Con el repo del W4** (`workshops/04-physical-ai-mcp-swarm/physical-ai-workshop`): sigue su README (cuenta de Hiveflow y API key, que **creas tú**; cada foto gasta tus créditos). Sin placa, usa la "Cámara virtual". No uses `provision.py` ni el firmware en placas ajenas.

## 5. Errores comunes

- Tratar una acción física como si fuera reversible.
- Una sola señal para disparar una alarma, o una frecuencia igual para riesgos distintos.
- Dejar un proyecto abierto a cualquier agente sin identidad ni forma de pedir cuentas.
- Mandar fotos de personas a un tercero sin pensar en su privacidad.

## 6. Preguntas de repaso

1. ¿Dónde ocurre el razonamiento: en la placa o en la nube? ¿Por qué?
2. ¿Por qué la frecuencia de revisión depende del riesgo?
3. ¿Qué problema trae un proyecto abierto a miles de agentes y cómo se mitigó?
4. ¿Qué comparte una "vacuna" y qué no?

<details><summary>Respuestas</summary>

1. En la nube (Claude); los modelos pequeños de la placa "no son tan inteligentes".
2. Porque el costo de tardar es distinto: fuego pide revisar cada segundo; una fuga pequeña, cada minuto.
3. No se sabe quién es cada agente ni a quién pedir cuentas; se mitigó dándole **un correo por agente** para ver qué hace.
4. Comparte el **patrón** del ataque (aprobado por una persona); no comparte datos personales.
</details>

## 7. Conecta con

- Anterior: [Módulo 4](04-controles-y-seguridad.md). Siguiente: [Módulo 6 · Evaluar y auditar](06-evaluar-y-auditar.md).
- Conceptos 18 a 20 de [conceptos.md](../conceptos.md).
