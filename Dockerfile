FROM python:3.6-slim

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN python handler/test.py