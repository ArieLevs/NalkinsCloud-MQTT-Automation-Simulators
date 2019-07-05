
FROM python:3.6-alpine

MAINTAINER Arie Lev

ENV PYTHONUNBUFFERED 1
ARG PYPI_REPO="https://pypi.python.org/simple"
ENV PYPI_REPO $PYPI_REPO

RUN mkdir /src
WORKDIR /src

ADD src /src/
RUN pip install \
    --index-url $PYPI_REPO \
    --requirement requirements.txt

# Cleanup
ENV PYPI_REPO 'None'

ENTRYPOINT ["python", "/src/start_service.py"]
