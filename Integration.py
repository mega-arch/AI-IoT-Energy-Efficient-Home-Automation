import paho.mqtt.client as mqtt
import json

# MQTT Broker details
broker = "mqtt.eclipse.org"
port = 1883
topic = "home/lighting/control"

# MQTT Client setup
client = mqtt.Client()

# Callback when connected to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Send the sensor data once connected
    payload = {
        "ambient_light": 350,
        "optimal_light_intensity": 150
    }
    client.publish(topic, json.dumps(payload))

# Connect to the broker
client.on_connect = on_connect
client.connect(broker, port, 60)

# Loop forever to maintain connection and handle messages
client.loop_forever()
