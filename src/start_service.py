
from threading import Thread
from mqtt_handler import MQTTClient
from configs import DEVICES
from logging_handler import logger
from configs import BROKER_HOST, BROKER_PORT, BROKER_TLS, BROKER_CERT


def init_simulator(device_id, device_pass, device_type, device_qos, topic, subscription_update):

    if device_type not in DEVICES:
        logger.error("Error: trying to init unknown simulator type - " + device_type)
        exit(1)
    else:
        logger.info("Starting new thread as device: " + device_id)

        mqtt_client = MQTTClient(broker_host=BROKER_HOST, broker_port=BROKER_PORT,
                                 broker_cert=BROKER_CERT, broker_tls=BROKER_TLS)
        mqtt_client.init_device(device_id=device_id,
                                device_password=device_pass,
                                device_type=device_type,
                                qos=device_qos,
                                topic=topic,
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
    for key, value in DEVICES.items():

        Thread(target=init_simulator,
               args=(value['device_user'],
                     value['device_pass'],
                     value['device_type'],
                     value['qos'],
                     value['topic'],
                     value['subscription_update']),
               name=value['device_user']).start()
