import paho.mqtt.client as mqtt

# Callback when connected to the broker
def on_connect(client, userdata, flags, rc, properties=None):
    print("✅ Connected to broker")
    client.subscribe("plc/voice_control")  # Subscribe to the topic

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"📥 Received message on topic '{msg.topic}': {msg.payload.decode()}")

# Setup MQTT client
client = mqtt.Client(protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

# Connect to local broker
client.connect("localhost", 1883, 60)

# Keep listening for messages
client.loop_forever()
