
FROM python:3.6-alpine

MAINTAINER Arie Lev

ENV PYTHONUNBUFFERED 1
RUN mkdir /nalkinscloud-mqtt-simulators
WORKDIR /nalkinscloud-mqtt-simulators

ADD src /nalkinscloud-mqtt-simulators
RUN pip install -r requirements.txt

ADD entrypoint.sh /nalkinscloud-mqtt-simulators
RUN chmod +x entrypoint.sh

RUN chmod 755 -R /nalkinscloud-mqtt-simulators

ENTRYPOINT ["sh", "/nalkinscloud-mqtt-simulators/entrypoint.sh"]
