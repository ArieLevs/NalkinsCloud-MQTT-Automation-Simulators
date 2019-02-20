

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import json
import ssl
import socket
import random
import os

host_name = "alpha.mosquitto.nalkins.cloud"
server_port = 1883
device_id = "test_switch_simulator"
device_password = "test_switch_simulator"

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
cert_location = BASE_DIR + "/certificates/alpha.mosquitto_server.crt"
topic = "test_switch_simulator/switch/status"

auth = {
  'username': device_id,
  'password': device_password
}

tls = {
  'ca_certs': cert_location,
  'tls_version': ssl.PROTOCOL_TLSv1_1
}


def publishmsg(top, msg):
    publish.single(topic=top,
                   payload=msg,
                   hostname=host_name,
                   auth=auth,
                   client_id=device_id,
                   port=server_port,
                   protocol=mqtt.MQTTv311,
                   retain=True)


temp = random.randint(10, 33)
text = 'offline'
data = {
    'host': socket.gethostname(),
    'short_message': text,
}

print("Publishing message")
#publishmsg(topic, json.dumps(text))
publishmsg(topic, text)
