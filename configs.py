
import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

mosquitto_host = 'nalkins.cloud'


class TemperatureConfigs(object):
    device_type = 'dht'
    mosquitto_host = ''
    mosquitto_port = 8883
    mosquitto_dht_user = 'test_dht_simulator'  # Device
    mosquitto_dht_pass = ''  # Device password
    qos = 1
    mosquitto_cert_location = '/etc/ssl/certs/mosquitto_server.crt'


class SwitchConfigs(object):
    device_type = 'switch'
    mosquitto_host = ''
    mosquitto_port = 8883
    mosquitto_switch_user = 'test_switch_simulator'  # Device
    mosquitto_switch_pass = ''  # Device password
    qos = 1
    mosquitto_cert_location = '/etc/ssl/certs/mosquitto_server.crt'
