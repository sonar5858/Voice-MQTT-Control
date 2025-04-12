import paho.mqtt.client as mqtt

client = mqtt.Client(protocol=mqtt.MQTTv311)

# Connect to local MQTT broker
client.connect("localhost", 1883, 60)

# Publish a test message to a topic
client.publish("plc/voice_control", "hiiie")  # You can change topic/message as needed

print("📡 Published '1' to topic 'plc/voice_control'")

client.disconnect()
