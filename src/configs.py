
import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

PROJECT_NAME = 'nalkinscloud-mqtt-simulators'
ENVIRONMENT = os.environ.get('environment', 'dev')

BROKER_HOST = os.environ.get('broker_host', 'localhost')
BROKER_PORT = int(os.environ.get('broker_port', 1883))
BROKER_TLS = bool(os.environ.get('broker_tls', False))
BROKER_CERT = BASE_DIR + "/certificates/mosquitto_server.crt"

DEVICES = {
    'dht': {
        'device_user': os.environ.get('dht_user', 'test_dht_simulator'),
        'device_pass': os.environ.get('dht_pass', 'nalkinscloud'),
        'device_type': 'dht',
        'topic': os.environ.get('dht_topic', 'test_dht_simulator'),
        'qos': int(os.environ.get('dht_qos', 1)),
        'subscription_update': 'update_now'
    },
    'switch': {
        'device_user': os.environ.get('switch_user', 'test_switch_simulator'),
        'device_pass': os.environ.get('switch_pass', 'nalkinscloud'),
        'device_type': 'switch',
        'topic': os.environ.get('switch_topic', 'test_switch_simulator'),
        'qos': int(os.environ.get('switch_qos', 1)),
        'subscription_update': 'change_switch'
    }
}

CONNECTION_RETURN_STATUS = {
    0: 'Connection successful',
    1: 'Connection refused - incorrect protocol version',
    2: 'Connection refused - invalid client identifier',
    3: 'Connection refused - server unavailable',
    4: 'Connection refused - bad username or password',
    5: 'Connection refused - not authorised'
}

######################
# LOGGING SETTINGS
######################
GRAYLOG_ENABLED = os.environ.get('graylog_enabled', False)
GRAYLOG_HOST = os.environ.get('graylog_host', 'localhost')
GRAYLOG_PORT = os.environ.get('graylog_port', 12201)
EXTRA_FIELDS = {'application': PROJECT_NAME, 'environment': ENVIRONMENT}
