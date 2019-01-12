

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import json
import ssl
import socket
import random
import os

host_name = "mosquitto.nalkins.cloud"
server_port = 8883
device_id = "test_switch_simulator"
device_password = "nalkinscloud"

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
cert_location = BASE_DIR + "/certificates/alpha.mosquitto_server.crt"
topic = "test_switch_simulator/switch/from_device_current_status"

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
                   tls=tls,
                   port=server_port,
                   protocol=mqtt.MQTTv311,
                   retain=True)


temp = random.randint(10, 33)
text = 0
data = {
    'host': socket.gethostname(),
    'short_message': text,
}

print("Publishing message")
publishmsg(topic, json.dumps(text))
