
import paho.mqtt.client as mqtt
from functions import is_valid_topic
from random import randint
import ssl
from logging_handler import logger
from datetime import datetime


CONNECTION_RETURN_STATUS = {
    0: 'Connection successful',
    1: 'Connection refused - incorrect protocol version',
    2: 'Connection refused - invalid client identifier',
    3: 'Connection refused - server unavailable',
    4: 'Connection refused - bad username or password',
    5: 'Connection refused - not authorised'
}


class MQTTClient(object):
    _broker_host = None
    _broker_port = None
    _broker_tls = None
    _broker_cert = None

    _device_id = None
    _device_type = None
    _qos = None
    _topic = None
    _subscription_update = None
    _mqtt_client = None

    def __init__(self, broker_host='127.0.0.1', broker_port=1883,
                 broker_tls=False, broker_cert=''):
        self._broker_host = broker_host
        self._broker_port = broker_port
        self._broker_cert = broker_cert
        self._broker_tls = broker_tls

    def init_device(self, device_id, device_type, device_password, qos, topic, subscription_update):
        self._device_id = device_id
        self._device_type = device_type
        self._qos = qos
        self._topic = topic
        self._subscription_update = subscription_update

        # Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv31)
        self._mqtt_client = mqtt.Client(client_id=device_id,
                                        clean_session=False,
                                        userdata={'device_id': device_id,
                                                  'device_type': device_type,
                                                  'qos': qos})

        self._mqtt_client.username_pw_set(username=device_id, password=device_password)

        if self._broker_tls:
            self._mqtt_client.tls_set(ca_certs=self._broker_cert, tls_version=ssl.PROTOCOL_TLSv1_1)

        if device_type is 'dht':
            self._mqtt_client.on_message = self.on_dht_message
        elif device_type is 'switch':
            self._mqtt_client.on_message = self.on_switch_message
        self._mqtt_client.on_connect = self.on_connect

    def get_mqtt_client(self):
        return self._mqtt_client

    # Set a Will (LWT) to be sent to the broker. If the client disconnects without calling disconnect(),
    # the broker will publish the message on its behalf.
    def set_lwt(self, device_id, device_type, qos, is_retained):  # Last Will and Testament
        self._mqtt_client.will_set(device_id + "/" + device_type + '/status',
                                   payload='offline',
                                   qos=qos,
                                   retain=is_retained)

    # connect the client to the broker, this is a blocking function.
    def connect(self):
        try:
            self._mqtt_client.connect(host=self._broker_host, port=self._broker_port, keepalive=60)
        except Exception as exc:
            logger.error('Connection Error: {}'.format(str(exc)) +
                         '. Host: ' + self._broker_host +
                         '. Port: ' + str(self._broker_port))
            exit(1)

    def subscribe(self, topic, qos):
        logger.info(str(datetime.now()) + " Subscribing to: " + topic)
        self._mqtt_client.subscribe(topic, qos=qos)

    def publish(self, topic, payload, qos):
        logger.info(str(datetime.now()) + " Publish: " + topic)
        self._mqtt_client.publish(topic, payload=payload, qos=qos, retain=False)

    def publish_retained(self, topic, payload, qos):
        # publish(topic, payload=None, qos=0, retain=False)
        logger.info(str(datetime.now()) + " Publish RETAINED: " + topic)
        self._mqtt_client.publish(topic, payload=payload, qos=qos, retain=True)

    def on_switch_message(self, client, userdata, msg):
        message_topic = msg.topic  # Get message topic
        message_payload = msg.payload.decode('UTF-8')  # Get message body
        qos = str(msg.qos)

        if is_valid_topic(message_topic):
            parsed_topic = message_topic.split('/')
            logger.info(str(datetime.now()) + " Incoming message for device_id: " + parsed_topic[0] +
                        "\n\tdevice_type: " + parsed_topic[1] +
                        "\n\tsubject: " + parsed_topic[2] +
                        "\n\tmessage_body: " + message_payload +
                        "\n\tqos: " + qos)

            self.publish_retained(
                topic=self._topic + "/" + self._device_type + "/from_device_current_status",
                payload=message_payload,
                qos=msg.qos)
        else:
            logger.error("Error: invalid topic received")

    def on_dht_message(self, client, userdata, msg):
        message_topic = msg.topic  # Get message topic
        message_payload = msg.payload.decode('UTF-8')  # Get message body
        qos = str(msg.qos)

        if is_valid_topic(message_topic):
            parsed_topic = message_topic.split('/')
            logger.info(str(datetime.now()) + " Incoming message for device_id: " + parsed_topic[0] +
                        "\n\tdevice_type: " + parsed_topic[1] +
                        "\n\tsubject: " + parsed_topic[2] +
                        "\n\tmessage_body: " + message_payload +
                        "\n\tqos: " + qos)

            temp = randint(10, 25)
            humidity = randint(20, 80)

            self.publish_retained(topic=self._topic + '/' + self._device_type + '/temperature',
                                  payload=temp,
                                  qos=self._qos)
            self.publish_retained(topic=self._topic + '/' + self._device_type + '/humidity',
                                  payload=humidity,
                                  qos=self._qos)
        else:
            logger.error("Error: invalid topic received")

    def on_dht_connect(self, mqttc, userdata, flags, rc):
        if rc is not 0:

            logger.error("Error: " + self._device_id +
                         ", " + CONNECTION_RETURN_STATUS.get(rc))
            exit(1)

        else:
            self.publish_retained(topic=self._topic + '/' + self._device_type + '/status',
                                  payload="online",
                                  qos=self._qos)
            self.subscribe(topic=self._topic + '/' + self._device_type + '/update_now',
                           qos=self._qos)
            logger.info(CONNECTION_RETURN_STATUS.get(rc))

    def on_connect(self, mqttc, userdata, flags, rc):
        if rc is not 0:

            logger.error("Error: " + self._device_id +
                         ", " + CONNECTION_RETURN_STATUS.get(rc))
            exit(1)

        else:
            self.publish_retained(topic=self._topic + '/' + self._device_type + '/status',
                                  payload="online",
                                  qos=self._qos)
            self.subscribe(topic=self._topic + '/' + self._device_type + '/' + self._subscription_update,
                           qos=self._qos)
            logger.info(str(datetime.now()) + " " + CONNECTION_RETURN_STATUS.get(rc))

    # Disconnect from the broker cleanly.
    # Using disconnect() will not result in a will (LWT) message being sent by the broker
    def __del__(self):
        self._mqtt_client.disconnect()

    # This is a blocking form of the network loop and will not return until the client calls disconnect().
    # It automatically handles reconnecting.
    def do_loop_forever(self):
        # loop_forever(timeout=1.0, max_packets=1)
        self._mqtt_client.loop_forever()
