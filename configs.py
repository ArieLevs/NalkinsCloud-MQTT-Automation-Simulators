
import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

mosquitto_host = 'nalkins.cloud'


class TemperatureConfigs(object):
    device_type = "dht"
    mosquitto_host = '127.0.0.1'
    mosquitto_port = 1883
    mosquitto_dht_user = 'test_dht_simulate'  # Device
    mosquitto_dht_pass = ''  # Device password
    qos = 1
    mosquitto_cert_location = "/etc/mosquitto/certs/mosquitto_server.crt"


class SwitchConfigs(object):
    device_type = "switch"
    mosquitto_host = '127.0.0.1'
    mosquitto_port = 1883
    mosquitto_switch_user = 'test_switch_simulate'  # Device
    mosquitto_switch_pass = ''  # Device password
    qos = 1
    mosquitto_cert_location = "/etc/mosquitto/certs/mosquitto_server.crt"
