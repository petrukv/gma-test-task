FROM python:3.12.2-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app

RUN pip install -r requirements.txt

COPY . /app