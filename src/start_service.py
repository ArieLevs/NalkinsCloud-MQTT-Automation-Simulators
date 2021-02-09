import os
from threading import Thread

from configs import BROKER_HOST, BROKER_PORT, BROKER_TLS, BROKER_CERT, BROKER_TLS_SKIP
from configs import DEVICES
from logging_handler import logger
from nalkinscloud_mqtt_python_client.mqtt_handler import MQTTClient

VERSION = os.environ.get('version', 'null')


def init_simulator(device_id, device_pass, device_type, device_qos, subscription_update):
    if device_type not in DEVICES:
        logger.error("Error: trying to init unknown simulator type - " + device_type)
        exit(1)
    else:
        logger.info("Starting new thread as device: " + device_id)
        logger.info("mqtt_client values: {}".format(
            {"broker_host": BROKER_HOST,
             "broker_port": BROKER_PORT,
             "broker_cert": BROKER_CERT,
             "broker_tls": BROKER_TLS,
             "broker_tls_skip": BROKER_TLS_SKIP}
        ))

        mqtt_client = MQTTClient(broker_host=BROKER_HOST, broker_port=BROKER_PORT,
                                 broker_cert=BROKER_CERT, broker_tls=BROKER_TLS, broker_tls_skip=BROKER_TLS_SKIP)
        mqtt_client.init_device(device_id=device_id,
                                device_password=device_pass,
                                device_type=device_type,
                                qos=device_qos,
                                subscription_update=subscription_update)
        mqtt_client.set_lwt(device_id=device_id,
                            device_type=device_type,
                            qos=device_qos,
                            is_retained=True)
        if not mqtt_client.connect():
            exit(1)
        mqtt_client.do_loop_forever()

        # If reached this point, then mqtt_client existed on some point, terminate
        exit(1)


if __name__ == '__main__':
    logger.info("Starting server with version: " + VERSION)

    for key, value in DEVICES.items():
        Thread(target=init_simulator,
               args=(value['device_user'],
                     value['device_pass'],
                     value['device_type'],
                     value['qos'],
                     value['subscription_update']),
               name=value['device_user']).start()
