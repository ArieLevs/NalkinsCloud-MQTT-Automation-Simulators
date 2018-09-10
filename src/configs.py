
import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

PROJECT_NAME = os.environ.get('project_name', 'nalkinscloud-mqtt-simulators')
ENVIRONMENT = os.environ.get('environment', 'dev')

broker_host = os.environ.get('broker_host', 'localhost')
broker_port = os.environ.get('broker_port', 1883)

DEVICES = {
    'dht': {
        'device_type': 'dht',
        'broker_host': broker_host,
        'broker_port': int(broker_port),
        'broker_user': os.environ.get('dht_user', 'test_dht_simulator'),
        'broker_pass': os.environ.get('dht_pass', 'nalkinscloud'),
        'topic': os.environ.get('dht_topic', 'test_dht_simulator'),
        'qos': int(os.environ.get('qos', 1)),
        'cert_location': os.environ.get('cert_location', BASE_DIR + "/certificates/alpha.mosquitto_server.crt")
    },
    'switch': {
        'device_type': 'switch',
        'broker_host': broker_host,
        'broker_port': int(broker_port),
        'broker_user': os.environ.get('switch_user', 'test_switch_simulator'),
        'broker_pass': os.environ.get('switch_pass', 'nalkinscloud'),
        'topic': os.environ.get('switch_topic', 'test_switch_simulator'),
        'qos': int(os.environ.get('qos', 1)),
        'cert_location': os.environ.get('cert_location', BASE_DIR + "/certificates/alpha.mosquitto_server.crt")
    }
}

######################
# LOGGING SETTINGS
######################
GRAYLOG_HOST = os.environ.get('graylog_host', 'localhost')
GRAYLOG_PORT = os.environ.get('graylog_port', 12201)
EXTRA_FIELDS = {'application': PROJECT_NAME, 'environment': ENVIRONMENT}
