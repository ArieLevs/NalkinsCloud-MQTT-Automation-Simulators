import unittest
from functions import is_valid_topic
from mqtt_handler import MQTTClient
from configs import *

valid_topic = 'some/valid/topic'
invalid_topic = 'invalid/topic'
invalid_topic2 = '//'
empty_topic = ''


class FunctionsTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_valid_topic(self):
        self.assertTrue(is_valid_topic(valid_topic))
        self.assertFalse(is_valid_topic(invalid_topic))
        self.assertFalse(is_valid_topic(invalid_topic2))
        self.assertFalse(is_valid_topic(empty_topic))
        self.assertFalse(is_valid_topic(None))


class MqttHandlerTest(unittest.TestCase):

    def setUp(self):
        self.device_id = DEVICES['dht']['device_user']
        self.device_pass = DEVICES['dht']['device_pass']
        self.device_type = DEVICES['dht']['device_type']
        self.device_qos = DEVICES['dht']['qos']
        self.topic = DEVICES['dht']['topic']
        self.subscription_update = DEVICES['dht']['subscription_update']

        # Define mqtt_client for current test case
        self.mqtt_client = MQTTClient(broker_host=BROKER_HOST, broker_port=BROKER_PORT,
                                      broker_cert=BROKER_CERT, broker_tls=BROKER_TLS)

        self.mqtt_client.init_device(device_id=self.device_id,
                                     device_password=self.device_pass,
                                     device_type=self.device_type,
                                     qos=self.device_qos,
                                     topic=self.topic,
                                     subscription_update=self.subscription_update)

    def test_init_device(self):
        self.assertEqual('test_dht_simulator', self.mqtt_client._device_id)

    def test_get_mqtt_client(self):
        self.assertEqual(self.mqtt_client.get_mqtt_client(), self.mqtt_client._mqtt_client)

    def test_set_lwt(self):
        self.assertFalse(self.mqtt_client._mqtt_client._will)
        self.mqtt_client.set_lwt(device_id=self.device_id,
                                 device_type=self.device_type,
                                 qos=self.device_qos,
                                 is_retained=True)
        self.assertTrue(self.mqtt_client._mqtt_client._will)

    def test_connect(self):
        # Try connecting to localhost (while no mqtt server is running)
        self.assertRaises(Exception, self.mqtt_client.connect())


if __name__ == '__main__':
    unittest.main()
