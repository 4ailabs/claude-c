# Physical AI + MCP + Swarm Protocol

**Ponente:** Jonathan Olvera (Founder & CTO, Hiveflow)

Claude operando hardware real, de un agente a un enjambre. El hardware lo ponen los organizadores.

## Sales con

- Tu propio MCP server que conecta Claude Code a hardware real: lees sensores y accionas dispositivos desde una conversación.
- Criterios para diseñar tools seguras cuando las acciones tienen consecuencias físicas.
- Swarm Protocol: ese agente convertido en un enjambre coordinado.
- El repo open source para replicarlo.

## En una frase

Claude con hardware real (una placa ESP32 con cámara) y agentes que se comunican entre sí, con un humano en el loop.

## Lo esencial

- Una placa **ve, pero no piensa**: manda la foto y Claude la describe en Hiveflow.
- Las acciones físicas tienen consecuencias: frecuencia y umbrales según el riesgo, bitácora y aprobación humana.
- "La siguiente ola": agentes que interactúan con agentes de otros. Pide identidad, trazabilidad y compartir lo aprendido sin compartir datos (las "vacunas").

## Qué hay en esta carpeta

| Archivo | Para qué |
|---|---|
| [`notas.md`](notas.md) | Lo que se dijo, en orden, con marcas `[hh:mm:ss]` y las dudas marcadas con (?) |
| [`preguntas.md`](preguntas.md) | Las **tres preguntas** para el ponente, sobre su experiencia (y una reserva) |
| [`tareas.md`](tareas.md) | La consigna, el plan y el avance de la práctica |
| [`physical-ai-workshop/`](physical-ai-workshop) | Repo del ponente ([hiveflowai/physical-ai-workshop](https://github.com/hiveflowai/physical-ai-workshop)); **no se versiona aquí** |
| Transcripción | `transcripts/04-physical-ai-mcp-swarm/`, **no se versiona** (lleva voces de asistentes) |

## Para retomarlo

Repo clonado y revisado, **sin ejecutar ni flashear nada**. Para hacer la práctica (según su README, unos 10 minutos):

1. Crear una cuenta en `app.hiveflow.ai/signup` y una **API token** en Perfil (**la creas tú**; cada foto gasta créditos de tu cuenta).
2. Con placa: plantilla **"Vigía con cámara · ESP32"**; sin placa: **"Cámara virtual · Vigía por chat"** y mandar una foto desde el teléfono.
3. Placa: unirte al Wi-Fi `Hive-mesa-N`, pegar primero la API key y luego el Wi-Fi.
4. Comprobar el reporte de Claude en la ejecución del flow.

## Estado

- [x] Notas (con el video de cierre como apéndice), preguntas y tareas.
- [x] Repo clonado y revisado.
- [ ] Cuenta de Hiveflow y API key (acción tuya).
- [ ] Probar con placa o con la cámara virtual.

> **Seguridad:** la placa guarda tu API key y tiene un pequeño servidor local; úsala en una red de confianza. `firmware/bin/*.bin` y `tools/provision.py` son para el organizador: no los uses en placas ajenas. El `skill.md` de SwarmMind hace que un agente se registre solo; revísalo antes de dárselo a uno.

**Para estudiar este tema:** [Módulo 5 · Mundo físico y enjambres](../../docs/estudio/05-mundo-fisico-y-enjambres.md) y el [4 · Controles y seguridad](../../docs/estudio/04-controles-y-seguridad.md).

Ver también: [guía final](../../docs/guia-final.md) · [conceptos](../../docs/conceptos.md) · [temario](../../docs/temario.md).
