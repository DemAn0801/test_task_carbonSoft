FROM python:3.10-slim

SHELL ["/bin/bash", "-c"]

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .
RUN pip install -r requierments.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
