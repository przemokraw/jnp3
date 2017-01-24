FROM python:3.5

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements ./requirements
RUN pip install -r requirements/production.txt

COPY . /code/

ADD uwsgi.ini /etc/uwsgi/django-uwsgi.ini

ADD db_check.py ./config/database-check.py

RUN adduser --no-create-home --disabled-login --group --system django
RUN chown -R django:django /code/

RUN ["chmod", "+x", "start.sh"]
CMD ["./start.sh"]
