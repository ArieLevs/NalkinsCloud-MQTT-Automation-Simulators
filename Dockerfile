
FROM python:3.6-alpine

MAINTAINER Arie Lev

ENV PYTHONUNBUFFERED 1
RUN mkdir /nalkinscloud-mqtt-simulators
WORKDIR /nalkinscloud-mqtt-simulators

ADD src /nalkinscloud-mqtt-simulators/
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/nalkinscloud-mqtt-simulators/start_service.py"]
