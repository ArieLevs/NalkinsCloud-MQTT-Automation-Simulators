
FROM python:3.6-alpine

MAINTAINER Arie Lev

ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src

ADD src /src/
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/src/start_service.py"]
