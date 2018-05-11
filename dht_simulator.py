
import datetime
import logging
from functions import *
from configs import *
from mqtt_handler import *

from random import randint

now = datetime.datetime.now()
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

general_topic = TemperatureConfigs.mosquitto_dht_user
logging.basicConfig(filename='/var/log/nalkinscloud_mqtt_simulators/dht_simulator.log', level=logging.DEBUG)


def on_message(client, userdata, msg):
    message_topic = msg.topic  # Get message topic
    message_payload = msg.payload.decode('UTF-8')  # Get message body
    qos = str(msg.qos)
    print("Incoming message - Topic: " + message_topic + "\tMessage: " + message_payload)
    logging.info("Incoming message - Topic: " + message_topic + "\tMessage: " + message_payload)
    if is_valid_topic(message_topic):
        parsed_topic = message_topic.split('/')
        logging.info("Incoming message - Device id: " + parsed_topic[0] +
                     "\tSensor type: " + parsed_topic[1] +
                     "\tSensors Data: " + parsed_topic[2] +
                     "\tMessage body: " + message_payload +
                     "\tQOS: " + qos)

        temp = randint(10, 25)
        humidity = randint(20, 80)

        # def publish_retained(self, topic, payload, qos):
        mqtt_client.publish_retained(general_topic + "/dht/temperature", payload=temp, qos=TemperatureConfigs.qos)
        mqtt_client.publish_retained(general_topic + "/dht/humidity", payload=humidity, qos=TemperatureConfigs.qos)

    else:
        print("ERROR - Invalid topic received")
        logging.error("ERROR - Invalid topic received")


def on_connect(self, client, userdata, rc):
    print("Connected with result code "+str(rc))
    logging.info("Connected with result code "+str(rc))
    mqtt_client.publish_retained(general_topic + "/dht/status", payload="online", qos=TemperatureConfigs.qos)
    mqtt_client.subscribe(general_topic + "/dht/update_now", qos=TemperatureConfigs.qos)

# def __init__(self, device_id, device_type, qos, device_password, cert_location):
mqtt_client = MQTTClient(TemperatureConfigs.mosquitto_dht_user,
                         TemperatureConfigs.device_type,
                         TemperatureConfigs.qos,
                         TemperatureConfigs.mosquitto_dht_pass,
                         TemperatureConfigs.mosquitto_cert_location)

# def set_lwt(self, device_id, device_type, qos, is_retained):
mqtt_client.set_lwt(TemperatureConfigs.mosquitto_dht_user,
                    TemperatureConfigs.device_type,
                    TemperatureConfigs.qos,
                    1)
mqtt_client.get_mqtt_client().on_message = on_message
mqtt_client.get_mqtt_client().on_connect = on_connect

# def connect(self, host_name, port):
mqtt_client.connect(TemperatureConfigs.mosquitto_host,
                    TemperatureConfigs.mosquitto_port)
mqtt_client.publish_retained(TemperatureConfigs.mosquitto_dht_user + "/" + TemperatureConfigs.device_type + "/status",
                             payload="online",
                             qos=TemperatureConfigs.qos,)

mqtt_client.get_mqtt_client().loop_forever()
