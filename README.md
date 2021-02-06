NalkinsCloud-MQTT-Automation-Simulators
=======================================

This repository will simulate NalkinsCloud end2end device, the code will simulate demo devices such as temperature sensors, smart switch etc. 
the network call is being made via DNS (or public IP), 
this means it simulates as real device coming from the public network.  

Docker container expects these env vars:
- environment
- broker_host
- broker_port
- broker_tls
- broker_tls_skip
- dht_user
- dht_pass
- dht_topic
- dht_qos
- switch_user
- switch_pass
- switch_topic
- switch_qos
- graylog_enabled
- graylog_host
- graylog_port

For deploying on Kubernetes view this [Helm chart](https://github.com/ArieLevs/Kubernetes-Helm-Charts/tree/master/charts/nalkinscloud-mqtt-simulators)

Build image
-----------
Create docker image   
```bash
docker build \
    --build-arg PYPI_REPO=https://nexus.nalkins.cloud/repository/pypi-repo/simple \
    -t docker.nalkins.cloud/nalkinscloud-mqtt-automation-simulators/nalkinscloud-mqtt-automation-simulators:latest .
```  

Upload 
```bash
docker push \
    docker.nalkins.cloud/nalkinscloud-mqtt-automation-simulators/nalkinscloud-mqtt-automation-simulators:latest
```
