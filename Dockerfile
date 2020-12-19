FROM python:3.8.6-slim

RUN apt-get update -qq
RUN apt-get install -y build-essential vim && \
        rm -rf /var/lib/apt/lists/*

RUN pip install -U pip
RUN pip install typed-ast

WORKDIR /app

RUN pip install flask flask-cors uwsgi requests wsgidav werkzeug
