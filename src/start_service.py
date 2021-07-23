import os
from threading import Thread
import random
import time
import json

from configs import BROKER_HOST, BROKER_PORT, BROKER_TLS, BROKER_CERT, BROKER_TLS_SKIP
from configs import DEVICES
from logging_handler import logger
from nalkinscloud_mqtt_python_client.devices import SwitchDevice, DHTDevice

VERSION = os.environ.get('version', 'null')


def get_dht_temp():
    return {"temperature": random.randint(10, 33), "humidity": random.randint(0, 100)}


def set_switch_state(state):
    logger.info("setting switch state to: {}".format(state))
    return state


def init_simulator(device_id, device_pass, device_type, device_qos):
    logger.info("mqtt_client values: {}".format(
        {"broker_host": BROKER_HOST,
         "broker_port": BROKER_PORT,
         "broker_cert": BROKER_CERT,
         "broker_tls": BROKER_TLS,
         "broker_tls_skip": BROKER_TLS_SKIP}
    ))

    if device_type == "switch":
        device = SwitchDevice(set_data_function=set_switch_state)
    elif device_type == "dht":
        device = DHTDevice(get_data_function=get_dht_temp)
    else:
        raise ValueError("trying to init unknown simulator type: {}".format(device_type))

    device.init_broker(broker_host=BROKER_HOST, broker_port=BROKER_PORT,
                       broker_cert=BROKER_CERT, broker_tls=BROKER_TLS, broker_tls_skip=BROKER_TLS_SKIP)

    device.init_device(device_id=device_id,
                       device_password=device_pass,
                       device_type=device_type,
                       qos=device_qos)

    # mqtt_client.set_lwt(device_id=device_id,
    #                    device_type=device_type,
    #                    qos=device_qos,
    #                    is_retained=True)
    if not device.connect():
        exit(1)

    if device_type == "dht":
        device.get_mqtt_client().loop_start()
        while True:
            device.publish(topic='v1/devices/me/telemetry',
                           payload=json.dumps(get_dht_temp()))
            time.sleep(60)
    else:
        device.do_loop_forever()

    # If reached this point, then mqtt_client existed on some point, terminate
    exit(1)


if __name__ == '__main__':
    logger.info("Starting server with version: " + VERSION)

    for key, value in DEVICES.items():
        Thread(target=init_simulator,
               args=(value['device_user'],
                     value['device_pass'],
                     value['device_type'],
                     value['qos']),
               name=value['device_user']).start()
