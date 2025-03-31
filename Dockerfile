FROM python:3.9

LABEL maintainer="foool1"
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        postgresql-client \
        libzbar0 \
        build-essential \
        libpq-dev \
        libzbar-dev \
        tesseract-ocr \
        libtesseract-dev \
        libjpeg-dev \
        zlib1g-dev \
        libpng-dev \
        poppler-utils && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt; fi && \
    apt-get purge -y --auto-remove \
        build-essential \
        libpq-dev \
        libzbar-dev \
        libjpeg-dev \
        zlib1g-dev \
        libpng-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"
USER django-user

