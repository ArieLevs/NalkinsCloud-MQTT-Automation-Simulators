
import os
from functions import is_valid_topic
from configs import DEVICES
from mqtt_handler import *

from random import randint
from graylog_logging import logger

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

general_topic = DEVICES['dht']['topic']


def on_message(client, userdata, msg):
    message_topic = msg.topic  # Get message topic
    message_payload = msg.payload.decode('UTF-8')  # Get message body
    qos = str(msg.qos)

    if is_valid_topic(message_topic):
        parsed_topic = message_topic.split('/')
        logger.info("Incoming message for device_id: " + parsed_topic[0] +
                    "\n\tdevice_type: " + parsed_topic[1] +
                    "\n\tsubject: " + parsed_topic[2] +
                    "\n\tmessage_body: " + message_payload +
                    "\n\tqos: " + qos)

        temp = randint(10, 25)
        humidity = randint(20, 80)

        mqtt_client.publish_retained(topic=general_topic + '/' + DEVICES['dht']['device_type'] + '/temperature',
                                     payload=temp,
                                     qos=DEVICES['dht']['qos'])
        mqtt_client.publish_retained(topic=general_topic + '/' + DEVICES['dht']['device_type'] + '/humidity',
                                     payload=humidity,
                                     qos=DEVICES['dht']['qos'])
    else:
        logger.error("Error: invalid topic received")


def on_connect(client, userdata, flags, rc):
    logger.info(DEVICES['dht']['broker_user'] + " connected with result code "+str(rc))
    mqtt_client.publish_retained(topic=general_topic + '/' + DEVICES['dht']['device_type'] + '/status',
                                 payload="online",
                                 qos=DEVICES['dht']['qos'])
    mqtt_client.subscribe(topic=general_topic + '/' + DEVICES['dht']['device_type'] + '/update_now',
                          qos=DEVICES['dht']['qos'])


mqtt_client = MQTTClient(device_id=DEVICES['dht']['broker_user'],
                         device_type=DEVICES['dht']['device_type'],
                         device_password=DEVICES['dht']['broker_pass'],
                         cert_location=DEVICES['dht']['cert_location'])

mqtt_client.set_lwt(device_id=DEVICES['dht']['broker_user'],
                    device_type=DEVICES['dht']['device_type'],
                    qos=DEVICES['dht']['qos'],
                    is_retained=1)

mqtt_client.get_mqtt_client().on_message = on_message
mqtt_client.get_mqtt_client().on_connect = on_connect

mqtt_client.connect(host_name=DEVICES['dht']['broker_host'],
                    port=DEVICES['dht']['broker_port'])

mqtt_client.get_mqtt_client().loop_forever()
