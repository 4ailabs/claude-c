# Notas · Physical AI + MCP + Swarm Protocol

**Ponente:** Jonathan Olvera (fundador de Hiveflow; en el audio suena "Highfield" / "HiFlu" (?)) · **Fuente:** `transcripts/04-physical-ai-mcp-swarm/sesion.md` (grabación `20261019 1922`, 36.6 min, 19:22–19:59).
**Repo:** `github.com/hiveflowai/physical-ai-workshop` (clonado en `workshops/04-physical-ai-mcp-swarm/physical-ai-workshop`).

> Convención: `[hh:mm:ss]` = marca de la transcripción. **(?)** = dudoso por la transcripción automática (nombres, cifras, términos técnicos). El README del repo se usó para contrastar nombres, pero lo citado con marca es lo que se dijo en el audio.

## Temas en el orden en que se dieron

### 1. Arranque: placas, regalo y networking `[00:00:00–00:03:12]`
- Reparto de las placas ESP32 (una por mesa) `[00:00:27–00:01:30]`. La placa se regala al final, a quien tenga más seguidores en LinkedIn en cada mesa (?) `[00:01:50–00:02:01]`.
- Primera idea: "no porque se pueda construir necesita ser construido" `[00:02:25]`. Lo que ha hecho tener éxito a sus startups es **conectar con humanos**, tener seguidores y exponer los proyectos `[00:02:31–00:03:08]`.

### 2. De qué va `[00:03:12–00:06:25]`
- Cómo Claude puede operar en el **mundo físico**, no solo el digital; tiene la documentación abierta de la mayoría de los dispositivos `[00:03:12–00:03:58]`.
- Plan: conectar *Physical AI* (la ESP32) con Claude, con MCP, y llegar al **enjambre** `[00:04:09–00:04:26]`.
- **"La siguiente ola":** ya hay un cerebro grande (el modelo), con manos (MCP) y agentes que tienen horarios y objetivos; lo siguiente es que **los agentes interactúen con los agentes de otras personas**. Eso trae nuevas preguntas de **protocolos de seguridad y de comunicación**, y nuevas herramientas para que los enjambres trabajen `[00:04:37–00:05:43]`.
- La cámara de la placa toma una foto y se manda a un enjambre para decidir si hay riesgo en el edificio `[00:06:03–00:06:16]`.

### 3. Quién es `[00:06:25–00:08:35]`
- Fundador de Hiveflow: "un sistema operativo donde humanos y agentes pueden trabajar" `[00:06:25]`. 15 años emprendiendo, **seis empresas fundadas y esta es la séptima**, "muchas cicatrices" `[00:06:36–00:06:52]`.
- Ingeniero industrial con especialidad en sistemas y finanzas `[00:07:14]`. Contó que el año pasado ganó el **primer lugar de un hackathon en Stanford** con unas 600 personas (afirmación suya) `[00:07:20–00:07:42]`. Mensaje: "si yo puedo, prácticamente todos pueden en Latinoamérica" `[00:07:49–00:08:06]`.

### 4. Por qué lo físico es distinto `[00:08:39–00:10:05]`
- El código que falla suele poder arreglarse; "¿qué pasa cuando se trata de una **válvula**?" Las consecuencias son mayores y afectan a personas `[00:08:43–00:09:21]`.
- Al poner un MCP y darle más trabajo al agente, "la responsabilidad cae en ti como programador o ingeniero"; por eso se definen parámetros y conviene **un humano en el loop** `[00:09:40–00:10:05]`.

### 5. Qué hace la placa `[00:10:05–00:12:00]`
- La ESP32 tiene Wi-Fi y Bluetooth `[00:10:30]`. Hay modelos pequeños que correrían en la placa, "pero no son tan inteligentes", así que la foto se manda a **Claude** `[00:10:19–00:10:28]`.
- "Una placa **ve, pero no piensa**" `[00:11:00]`. Se le pueden agregar sensores, pero por sí solos solo detectan encendido/apagado o un valor (humedad, luz) `[00:11:19–00:11:33]`.

### 6. Preparación de la placa `[00:12:03–00:13:57]`
1. Cable USB a la ESP32 `[00:12:03–00:12:13]`.
2. Al darle energía, la placa abre **su propio Wi-Fi, uno por mesa** (la etiqueta trae el número) `[00:12:36–00:12:53]`.
3. Al conectarte sale una pantalla donde se capturan **el Wi-Fi, su contraseña y una API key** `[00:13:00–00:13:14]`; es "la parte risky" `[00:13:14]`.
4. La API key sale de una cuenta en Hiveflow, a la que se llega por un **QR** `[00:13:26–00:13:50]`.

### 7. Idea para hacer en casa `[00:15:01–00:16:56]`
Conectar la ESP32 a la computadora y pedirle a Claude "defíneme cómo leer los sensores"; con herramientas web (Context7) puede traer la documentación y **conversar directamente con la placa** `[00:15:01–00:15:33]`. Con la placa se puede tomar foto y subir el brillo de los LEDs `[00:15:44]`; se pueden construir **MCP alrededor de la placa** para leerla de forma conversacional `[00:16:18–00:16:46]`.

### 8. Cómo definir los controles `[00:17:25–00:18:23]`
- **Definir las consecuencias físicas:** valores "rojos" (fuego), **frecuencia y alcance**: si hay riesgo de fuego quizá cada segundo; una fuga de agua no tan riesgosa, cada minuto `[00:17:25–00:17:46]`.
- Aunque la IA pueda decidir, **un humano** debe poder confirmar si está pasando o no, y llevar una **bitácora** `[00:17:57–00:18:23]`.

### 9. Enjambres y protocolos entre agentes `[00:18:23–00:22:45]`
- Hiveflow publicó dos proyectos para conectar un MCP con otros agentes "de forma segura y trazable"; en el audio suenan "FarmMind" y "FarmOut" (?) `[00:18:23–00:18:53]` (el nombre de uno coincide con SwarmMind, `swarmind.sh`).
- Un proyecto público donde los agentes entran a un canal con tablero (por hacer, haciendo, hecho) `[00:19:02–00:19:37]`. Estaba **abierto a cualquier agente**: en la primera semana llegaron **unos 3,000 agentes** que empezaron a construir tableros (cifra dudosa) `[00:19:45–00:20:04]`.
- El problema: si quieres responsabilizar a uno de esos agentes, ¿con quién hablas? La solución: **un correo por cada agente** que permite ver qué hace `[00:20:09–00:20:35]`.
- **Simulación de enjambre:** alguien detecta humo, otro una puerta abierta; el enjambre espera varias aprobaciones y, si **dos o tres criterios** apuntan a una emergencia, **pide permiso a un humano** antes de actuar `[00:20:46–00:21:33]`.
- **Protección entre agentes:** si un nodo "se infecta", aprende y **comparte** lo ocurrido con la red, como una vacuna; así se protege al resto `[00:21:33–00:22:45]`. Menciona que "me pasó con agentes chinos" (?) `[00:21:37]`.

### 10. La práctica `[00:22:51–00:33:51]`
- Repo: `github.com/hiveflowai/physical-ai-workshop` `[00:22:51]`.
- **Cuenta en Hiveflow:** al registrarse dan **5 dólares de crédito** (en "Club" (?)) `[00:23:11–00:23:22]`; en **Perfil** se genera un **API token** que se copia y se guarda `[00:23:22–00:23:48]`.
- **Con placa:** Templates → plantilla ESP32 → clonar; **sin placa:** plantilla "Vigía virtual", que sube una imagen por chat `[00:23:54–00:24:47]`.
- **Placa:** unirse al Wi-Fi `Hive-mesa-N`; la ruta (IP) muestra una bienvenida y la cámara `[00:25:22–00:25:57]`; se elige la red del evento ("Otoño 26" (?)) y su contraseña `[00:27:07–00:27:10]`; hay que registrarse primero para tener la API key `[00:27:20–00:27:31]`. Al guardar aparece "detectado" y la URL permite **ver la cámara en tiempo real** `[00:27:51–00:28:15]`.
- La placa **manda una foto cuando cambia la escena** `[00:28:19–00:28:24]`.
- **En vivo:** llegaron unas 36 peticiones; alguien mandó un escenario con pantalla roja; algunas llegaron a **alerta por correo**, incluida una foto de fuego del propio ponente `[00:28:38–00:29:46]` · `[00:32:09]`.
- **Cámara virtual:** publicar el flow, abrir el chat desde el teléfono y mandar una foto; no devuelve nada del modelo, porque la placa solo envía `[00:29:46–00:31:12]`.
- **Flow "Vigía":** el modelo es de Anthropic; recibe la foto, el nodo, qué ve y el texto, evalúa riesgo (p. ej. derrame) y lo manda a un **portal de enjambre** `[00:31:19–00:32:01]`. La alerta fue un correo, pero se puede conectar WhatsApp, Telegram o Slack `[00:32:52–00:33:12]`.
- Todo el flujo se creó **de forma conversacional**; hay un conector de Hiveflow para Claude y ChatGPT (un **MCP**) para construirlo hablando `[00:33:12–00:33:51]`.

### 11. Cierre `[00:34:14–00:36:29]`
- "**El modelo puede equivocarse**"; el modelo por sí solo no basta: se necesitan filtros y **humano en el loop** `[00:34:20–00:34:51]`. Ejemplo: te llega una notificación al celular, ves la imagen y apruebas o rechazas `[00:35:06–00:35:13]`.
- Riesgo de la **caja negra**: construir con IA "funciona como magia", pero a un compañero no técnico es difícil mostrarle dónde se atoró; por eso buscan "lo mejor de los dos mundos": lo agéntico y lo **visual para humanos** `[00:35:18–00:36:21]`.

## Apéndice: video de cierre (está en la grabación del workshop 5)

Al inicio de `transcripts/05-del-agente-al-equipo/sesion.md` el ponente pasó un video (marcas `W5 [hh:mm:ss]`) con una simulación de **enjambre entre hospitales**, que ilustra la idea de "cuando uno aprende, todos quedan protegidos". Los nombres propios salen distorsionados; se marcan con (?).
- **Idea:** cada paciente tiene un "ayudante" (agente delegado) en su hospital que **nunca firma nada sin permiso de su humano**; si descubre una trampa, **avisa a los demás hospitales sin contar los secretos, solo cómo es la trampa** `W5 [00:00:19–00:00:50]`.
- **Piezas del mapa:** cada hospital es un *supernode* (Flower (?)) donde viven los datos del paciente y **nunca salen**; cada agente piensa con un modelo servido por un proveedor (Kimi o Minimax en Nebius (?)); hay un coordinador central que reparte los mensajes y junta las respuestas; un consorcio de investigación (Stanford) hace de **remitente honesto**; los **impostores**, como una falsa agencia federal, **no tienen identidad firmada y se rechazan en la puerta** `W5 [00:00:53–00:01:49]`.
- **Defensas en capas** `W5 [00:01:49–00:02:45]`:
  1. Un **filtro rápido** (TypeSafe (?)) que frena un ataque obvio antes de que lo lea un modelo grande.
  2. Un **mandato firmado**: el modelo solo propone, pagar a una cuenta desconocida está prohibido y todo compromiso necesita tu firma desde el celular.
  3. Las **vacunas**: el patrón de un ataque, aprobado por una persona, que viaja a todos los hospitales sin llevar ningún dato.
  4. Cada mensaje va firmado con **Swarmind** y cada decisión queda en una **bitácora encadenada** que un regulador puede verificar.
  - Reparto: Flower pone la federación, Nebius los modelos, TypeSafe el filtro y Hiveflow **la identidad y la confianza entre agentes**.
- **La demo, en 5 rondas** `W5 [00:02:45–00:03:50]`: (1) solo llega la invitación de Stanford y los datos se quedan en el hospital; (2) la primera estafa, una cura milagrosa: cinco ayudantes caen, pero el mandato bloquea el pago y el hospital propone vacunas que tú apruebas; (3) nuevas variantes y un intento de robo de genoma: **las vacunas frenan 16 ataques antes de que los vea un modelo**; (4) una inyección de prompt y una falsa agencia: el impostor se rechaza en la puerta y ningún ayudante cae; (5) vuelven las estafas: **con la federación, cero engañados; si cada hospital atendiera solo, 12**. En las cinco rondas, **cero acciones dañinas y cero datos personales transferidos**.
- **Para qué:** útil en industrias como la financiera, donde en red y de forma descentralizada **no compartes la información de tus usuarios** pero sí cómo fue el ataque `W5 [00:03:50–00:04:26]`.
- Esto ocurre dentro de una **simulación**: las cifras (16 y 12) son del video del ponente y no se verificaron.

## Código y comandos mencionados
- Repo `physical-ai-workshop`; sin comandos en el audio (se sigue la guía del README).
- Pasos: cuenta en Hiveflow → API token → plantilla (ESP32 o "Vigía virtual") → Wi-Fi `Hive-mesa-N` → API key y Wi-Fi del evento → comprobar el reporte `[00:23:11–00:28:15]`.

## Dudas abiertas
- Nombres: "Highfield/HiFlu" (Hiveflow), "FarmMind/FarmOut" (SwarmMind / ?), y quién era "el león" `[00:00:19]`.
- Cifras: ~3,000 agentes en la primera semana, ~600 asistentes al hackathon de Stanford, 36 peticiones y 5 dólares de crédito.
- Regla del regalo de la placa (más seguidores en LinkedIn por mesa) `[00:01:50]`.
- Qué quiso decir con "agentes chinos" `[00:21:37]` y con tableros "chinos" `[00:20:04]`.
- El usuario y contraseña del Wi-Fi del evento no se oyen bien `[00:26:03–00:27:10]`.
