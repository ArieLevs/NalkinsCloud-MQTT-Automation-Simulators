

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import json
import ssl
import socket
import random
import os

host_name = "mosquitto.alpha.nalkins.cloud"
server_port = 8883
device_id = "publish_single"
device_password = "publish_single"

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
cert_location = BASE_DIR + "/certificates/mosquitto_server.crt"
topic = "test_dht_device_id/dht/temperature"

auth = {
  'username': device_id,
  'password': device_password
}

tls = {
    'insecure': True,
    'ca_certs': None,
    'cert_reqs': ssl.CERT_NONE,
    'tls_version': ssl.PROTOCOL_TLSv1_2,
}


def publishmsg(top, msg):
    publish.single(topic=top,
                   payload=msg,
                   hostname=host_name,
                   auth=auth,
                   client_id=device_id,
                   port=server_port,
                   protocol=mqtt.MQTTv311,
                   retain=True,
                   tls=tls)


temp = random.randint(10, 33)
text = 'offline'
data = {
    'host': socket.gethostname(),
    'short_message': text,
}

print("Publishing message")
#publishmsg(topic, json.dumps(text))
publishmsg(topic, temp)
