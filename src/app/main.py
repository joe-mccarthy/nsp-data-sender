from app.mqtt.mqtt_listener import MQTTListener, message_handler
import time
import os
import json

from .configuration.data import Configuration, get_single_configuration
from .senders.sender import FileUploaderFactory

temp_data = ".nsp-data-sender"

def load_json_files(directory):
    json_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.json')]
    json_files.sort(key=lambda x: os.path.getmtime(x))  # Sort by modification time, oldest first
    data = []
    for file_path in json_files:
        with open(file_path, 'r') as file:
            data.append(json.load(file))
    return data

def run(arguments):
    print(arguments)
    print("Running application")
    listener = MQTTListener(
        broker="127.0.0.1",
        port=1883,
        topic="nsp/archive-completed",
        on_message_callback=message_handler,
    )
    listener.start_listening()

    while True:
        json_data = load_json_files(temp_data)
        for json in json_data:
            config = get_single_configuration(temp_data, json['sender_id'])
            if config:
                config.file_path = json['file_path']            
                uploader = FileUploaderFactory.get_uploader(uploader_type=config.type, **config.__dict__)
                result = uploader.upload_file()
                if not result:
                    file = temp_data + '/' + json['file_name'] + '-' + json['sender_id'] + '.json'
                    os.remove(file)
                
        time.sleep(60)
        print("Running other tasks")
