FROM python:3.7
ENV PYTHONUNBUFFERED 1

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
RUN pip install -U pip setuptools

RUN mkdir -p /opt/project/src
WORKDIR /opt/project/src

COPY requirements.txt /opt/project/src
RUN pip install -r /opt/project/src/requirements.txt

ADD . /opt/project/src
# Django service
EXPOSE 8000
