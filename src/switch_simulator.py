
import datetime
from graylog_logging import logger
from functions import *
from configs import *
from mqtt_handler import *

now = datetime.datetime.now()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

general_topic = DEVICES['switch']['topic']


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

        mqtt_client.publish_retained(
            topic=general_topic + "/" + DEVICES['switch']['device_type'] + "/from_device_current_status",
            payload=message_payload,
            qos=DEVICES['switch']['qos'])
    else:
        logger.error("Error: invalid topic received")


def on_connect(mqttc, userdata, flags, rc):
    logger.info(DEVICES['switch']['broker_user'] + " connected with result code "+str(rc))
    mqtt_client.publish_retained(topic=general_topic + '/' + DEVICES['switch']['device_type'] + '/status',
                                 payload="online",
                                 qos=DEVICES['switch']['qos'])
    mqtt_client.subscribe(topic=general_topic + '/' + DEVICES['switch']['device_type'] + '/change_switch',
                          qos=DEVICES['switch']['qos'])


mqtt_client = MQTTClient(device_id=DEVICES['switch']['broker_user'],
                         device_type=DEVICES['switch']['device_type'],
                         device_password=DEVICES['switch']['broker_pass'],
                         cert_location=DEVICES['switch']['cert_location'])

mqtt_client.set_lwt(device_id=DEVICES['switch']['broker_user'],
                    device_type=DEVICES['switch']['device_type'],
                    qos=DEVICES['switch']['qos'],
                    is_retained=1)

mqtt_client.get_mqtt_client().on_message = on_message
mqtt_client.get_mqtt_client().on_connect = on_connect

mqtt_client.connect(host_name=DEVICES['switch']['broker_host'],
                    port=DEVICES['switch']['broker_port'])

mqtt_client.get_mqtt_client().loop_forever()
