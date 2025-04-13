import speech_recognition as sr
import paho.mqtt.client as mqtt
from Test_whatsapp import send_whatsapp_alert

# ----------------------
# MQTT Setup
# ----------------------
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "plc/voice_control"

mqtt_client = mqtt.Client(protocol=mqtt.MQTTv311)
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

# ----------------------
# Voice Setup
# ----------------------
recognizer = sr.Recognizer()
mic = sr.Microphone()

print("🎙️ Voice control active — Say 'hello start' or 'hello stop'")
print("Press Ctrl+C to stop.")

while True:
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("\n🔊 Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"🧠 You said: {command}")

        if "hello start" in command:
            mqtt_client.publish(MQTT_TOPIC, "1")
            print("✅ Published: 1 (START)")
            send_whatsapp_alert(" Voice command received: START the machine.")

        elif "hello stop" in command:
            mqtt_client.publish(MQTT_TOPIC, "0")
            print("🛑 Published: 0 (STOP)")
            send_whatsapp_alert("🛑 Voice command received: STOP the machine.")

        else:
            print("⏸️ Ignored — no valid command found.")

    except sr.UnknownValueError:
        print("🤷 Couldn't understand the audio.")
    except sr.RequestError as e:
        print(f"⚠️ Google API error: {e}")
