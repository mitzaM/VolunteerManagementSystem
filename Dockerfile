FROM python:3.9.6-buster

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip -r /tmp/requirements.txt && \
    rm -f /tmp/requirements.txt

RUN apt-get update && apt-get -y install postgresql-client

COPY . /code
WORKDIR /code
