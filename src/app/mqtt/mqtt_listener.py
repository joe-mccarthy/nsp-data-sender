import paho.mqtt.client as mqtt
import threading
import os
import json

from ..configuration.data import Configuration, get_configurations
from ..senders.sender import FileUploaderFactory

temp_data = ".nsp-data-sender"

class MQTTListener:
    def __init__(self, broker, port, topic, on_message_callback, keepalive=60):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.on_message_callback = on_message_callback
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.keepalive = keepalive

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f"Connected to MQTT Broker: {self.broker}")
            client.subscribe(self.topic)
        else:
            print(f"Failed to connect, return code {rc}")

    def on_message(self, client, userdata, msg):
        try:
            message_json = json.loads(msg.payload.decode())
            self.on_message_callback(msg.topic, message_json)
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON message: {e}")

    def start_listening(self):
        self.client.connect(self.broker, self.port, self.keepalive)
        thread = threading.Thread(target=self.client.loop_forever)
        thread.daemon = True
        thread.start()


# Example usage:
def message_handler(topic, message):

    print(f"Received message from topic {topic}: {message}")
    configurations = get_configurations("replace-me")
    config: Configuration
    for config in configurations:
        config.file_path = message.get("path")
        config.file_name = message.get("name")
        sender = FileUploaderFactory.get_uploader(
            uploader_type=config.type, **config.__dict__
        )
        json_output = sender.to_json()
        os.makedirs(temp_data, exist_ok=True)
        filename = message.get("name")
        output = f"{filename}-{config.id}.json"
        file_path = os.path.join(temp_data, output)
        with open(file_path, 'w') as file:
            file.write(json_output)

        # create a json file for the file and configuration to be uploaded in data folder


# listener = MQTTListener(broker='mqtt.example.com', port=1883, topic='test/topic', on_message_callback=message_handler)
# listener.start_listening()

# The script will continue running other tasks while listening for MQTT messages
