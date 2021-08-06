
import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

PROJECT_NAME = 'nalkinscloud-mqtt-simulators'
ENVIRONMENT = os.environ.get('environment', 'dev')
LOGGING_EXTRA_FIELDS = {'application': PROJECT_NAME, 'environment': ENVIRONMENT}

BROKER_HOST = os.environ.get('broker_host', 'localhost')
BROKER_PORT = int(os.environ.get('broker_port', 1883))
BROKER_TLS = bool(os.environ.get('broker_tls', False) in ["true", "True"])
BROKER_CERT = None
BROKER_TLS_SKIP = bool(os.environ.get('broker_tls_skip', False) in ["true", "True"])

DEVICES = {
    'dht': {
        'device_user': os.environ.get('dht_user', 'test_dht_simulator'),
        'device_pass': os.environ.get('dht_pass', 'nalkinscloud'),
        'device_type': 'dht',
        'qos': int(os.environ.get('dht_qos', 1)),
        'subscription_update': 'update_now'
    },
    'switch': {
        'device_user': os.environ.get('switch_user', 'test_switch_simulator'),
        'device_pass': os.environ.get('switch_pass', 'nalkinscloud'),
        'device_type': 'switch',
        'qos': int(os.environ.get('switch_qos', 1)),
        'subscription_update': 'change_switch'
    }
}

