# 🎙️ Voice-MQTT-Control 🔧

A modular Python-based voice command system integrated with MQTT and WhatsApp — built for industrial automation, real-time machine control, and operator notification.

## 🚀 Features

- ✅ Voice-controlled machine start/stop using simple phrases
- ✅ MQTT message publishing for PLC or HMI integration
- ✅ WhatsApp alerts to supervisors when voice commands are triggered
- ✅ Secure `.env` configuration for all sensitive credentials
- ✅ Fully local setup (optional Vosk support coming soon!)

---

## 💡 Use Case

This system is ideal for industrial environments where:

- Hands-free operation is preferred (e.g., safety zones)
- Supervisors need real-time alerts (e.g., fault, stop, emergency)
- Machines use PLCs or MQTT-based SCADA systems

---

## 🎯 Voice Commands

| Command           | MQTT Action         | WhatsApp Message                  |
|-------------------|---------------------|-----------------------------------|
| `hello start`     | Publishes `"1"`     | ✅ “Machine started by voice”     |
| `hello stop`      | Publishes `"0"`     | 🛑 “Machine stopped by voice”     |

---

## 🧱 Tech Stack

- 🐍 Python 3.11
- 🎙 SpeechRecognition + Google Speech API
- 📡 Paho-MQTT
- 💬 Twilio WhatsApp API
- 🔐 dotenv (.env) for secrets

---

## 🔐 .env File Setup

