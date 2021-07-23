import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import json
import ssl
import random
import os

broker_host = "thingsboard.nalkins.cloud"
broker_port = 1883
device_id = "11f4ef90-eabf-11eb-9d43-c556d75f85d1"
# device_password = "publish_single"
access_token = "d1uJtJc6184iobxJ52rG"

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
cert_location = BASE_DIR + "/certificates/mosquitto_server.crt"
topic = "v1/devices/me/telemetry"

auth = {
    'username': access_token
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
                   qos=1,
                   hostname=broker_host,
                   auth=auth,
                   client_id=device_id,
                   port=broker_port,
                   protocol=mqtt.MQTTv311,
                   retain=True,
                   tls=None)


temp = random.randint(10, 33)
text = 'offline'
data = {"temperature": random.randint(10, 33), "humidity": random.randint(0, 100)}

print("Publishing message")
publishmsg(topic, json.dumps(data))
