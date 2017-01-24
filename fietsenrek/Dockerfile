FROM python:3.5

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements ./requirements

RUN pip install -r requirements/production.txt

COPY . /code/
