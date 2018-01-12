import paho.mqtt.client as mqtt
import ssl


class MQTTClient(object):

    _mqtt_client = None
    _device_id = None
    _device_type = None

    def __init__(self, device_id, device_type, qos, device_password, cert_location):
        # Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv31)
        self._mqtt_client = mqtt.Client(client_id=device_id, clean_session=False,
                                        userdata=None)
        self._device_id = device_id
        self._device_type = device_type

        # Set function that will execute once client received a new message from broker
        def on_message(client, userdata, msg):
            print("New message from " + str(client) + " " + str(userdata))
            print(msg.topic + " " + msg.payload.decode('UTF-8'))

        # Set function that will execute once client connected to broker
        def on_connect(self, client, userdata, rc):
            print("Client: " + str(client) + ", User data: " + str(userdata))
            print("Connected with result code " + str(rc))

        # Set 'on_message' to the function above
        self._mqtt_client.on_message = on_message

        # Set 'on_connect' to the function above
        self._mqtt_client.on_connect = on_connect

        # username_pw_set(username, password=None)
        self._mqtt_client.username_pw_set(device_id, password=device_password)

        # tls_set(ca_certs, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
        #         tls_version=ssl.PROTOCOL_TLSv1, ciphers=None)
        self._mqtt_client.tls_set(ca_certs=cert_location, tls_version=ssl.PROTOCOL_TLSv1_1)

    def get_mqtt_client(self):
        return self._mqtt_client

    # Set a Will (LWT) to be sent to the broker. If the client disconnects without calling disconnect(),
    # the broker will publish the message on its behalf.
    def set_lwt(self, device_id, device_type, qos, is_retained):  # Last Will and Testament
        # will_set(topic, payload=None, qos=0, retain=False)
        self._mqtt_client.will_set(device_id + "/" + device_type + '/status', payload='offline',
                                   qos=qos, retain=is_retained)

    # Function connects the client to a broker. This is a blocking function.
    def connect(self, host_name, port):
        # connect_async(host, port=1883, keepalive=60, bind_address="")
        self._mqtt_client.connect(host_name, port=port, keepalive=60)

    # Subscribe the client to one or more topics
    def subscribe(self, topic, qos):
        # subscribe(topic, qos=0)
        self._mqtt_client.subscribe(topic, qos=qos)

    # Function causes a message to be sent to the broker
    def publish(self, topic, payload, qos):
        # publish(topic, payload=None, qos=0, retain=False)
        self._mqtt_client.publish(topic, payload=payload, qos=qos, retain=False)

    def publish_retained(self, topic, payload, qos):
        # publish(topic, payload=None, qos=0, retain=False)
        self._mqtt_client.publish(topic, payload=payload, qos=qos, retain=True)

    # Disconnect from the broker cleanly.
    # Using disconnect() will not result in a will (LWT) message being sent by the broker
    def __del__(self):
        self._mqtt_client.disconnect()

    # This is a blocking form of the network loop and will not return until the client calls disconnect().
    # It automatically handles reconnecting.
    def do_loop_forever(self):
        # loop_forever(timeout=1.0, max_packets=1)
        self._mqtt_client.loop_forever()
