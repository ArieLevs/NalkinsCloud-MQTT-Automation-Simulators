NalkinsCloud-MQTT-Automation-Simulators
=======================================

This repo will simulate NalkinsCloud end device, the code will simulate demo devices such as temperature sensors, smart switch etc. the network call is being made via DNS, this means it simulates as real device coming from the outside.  
In order for the code to successfully execute, `config.py` file must be changed with relevant info.

for example, in order for the temperature device simulator to connect to Mosquitto Server, it should look like this:
```
class TemperatureConfigs(object):
    device_type = "dht"
    mosquitto_host = '[SAME DOMAIN CERTIFICATED CREATED WITH]'  # This is must or handshake will fail
    mosquitto_port = 8883  # TLS port
    mosquitto_dht_user = 'test_dht_simulate'  # Device
    mosquitto_dht_pass = '[PASSWORD OF test_dht_simulate IN DB]'  # Device password
    qos = 1
    mosquitto_cert_location = "/etc/mosquitto/certs/mosquitto_server.crt"
```

* Please note that this done is automatically configured as part of [NalkinsCloud Project](https://github.com/ArieLevs/NalkinsCloud)
