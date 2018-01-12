NalkinsCloud-MQTT-Automation-Simulators
=======================================

This repo will simulate NalkinsCloud end device, the code will simulate demo devices such as temperature sensors, smart switch etc.  
In order for the code to successfully execute, `config.py` file must be changed with relevant info.

for example, in order for the temperature device simulator to connect to Mosquitto Server, it should look like this:
```
class TemperatureConfigs(object):
    device_type = "dht"
    mosquitto_host = '127.0.0.1'
    mosquitto_port = 1883
    mosquitto_dht_user = 'test_dht_simulate'  # Device
    mosquitto_dht_pass = '[PASSWORD OF test_dht_simulate IN DB]'  # Device password
    qos = 1
    mosquitto_cert_location = "/etc/mosquitto/certs/mosquitto_server.crt"
```

* Please note that this done is automatically configured as part of [NalkinsCloud Project](https://github.com/ArieLevs/NalkinsCloud)
