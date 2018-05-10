
import datetime
import logging
from functions import *
from configs import *
from mqtt_handler import *
from threading import Thread

now = datetime.datetime.now()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

general_topic = SwitchConfigs.mosquitto_switch_user
logging.basicConfig(filename=BASE_DIR + '/logs/test_switch.log', level=logging.DEBUG)


def threaded_function(message_payload):
    print("Running threaded_function")
    # def publish_retained(self, topic, payload, qos):
    mqtt_client.publish_retained(SwitchConfigs.mosquitto_switch_user + "/" + SwitchConfigs.device_type + "/from_device_current_status",
                                 payload=message_payload,
                                 qos=SwitchConfigs.qos)


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

        thread = Thread(target=threaded_function, args=(message_payload,))
        thread.start()
        thread.join()
    else:
        print("ERROR - Invalid topic received")
        logging.error("ERROR - Invalid topic received")


def on_connect(self, client, userdata, rc):
    print("Connected with result code "+str(rc))
    logging.info("Connected with result code "+str(rc))
    mqtt_client.publish_retained(SwitchConfigs.mosquitto_switch_user + "/" + SwitchConfigs.device_type + "/status",
                                 payload="online",
                                 qos=SwitchConfigs.qos)
    mqtt_client.subscribe(SwitchConfigs.mosquitto_switch_user + "/" + SwitchConfigs.device_type + "/change_switch",
                          qos=SwitchConfigs.qos)


# def __init__(self, device_id, device_type, qos, device_password, cert_location):
mqtt_client = MQTTClient(SwitchConfigs.mosquitto_switch_user,
                         SwitchConfigs.device_type,
                         SwitchConfigs.qos,
                         SwitchConfigs.mosquitto_switch_pass,
                         SwitchConfigs.mosquitto_cert_location)

# def set_lwt(self, device_id, device_type, qos, is_retained):
mqtt_client.set_lwt(SwitchConfigs.mosquitto_switch_user,
                    SwitchConfigs.device_type,
                    SwitchConfigs.qos,
                    1)
mqtt_client.get_mqtt_client().on_message = on_message
mqtt_client.get_mqtt_client().on_connect = on_connect

# def connect(self, host_name, port):
mqtt_client.connect(SwitchConfigs.mosquitto_host,
                    SwitchConfigs.mosquitto_port)

mqtt_client.get_mqtt_client().loop_forever()
