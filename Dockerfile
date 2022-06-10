FROM python:3.7.2
LABEL maintainer="andreas.wombacher@aureliusenterprise.com"

RUN pip install pipenv

ADD . /rest-services
WORKDIR /rest-services

RUN pipenv install --system --skip-lock

RUN pip install gunicorn[gevent]


EXPOSE 5000

CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level debug
# CMD gunicorn --bind 127.0.0.1:5000 wsgi --access-logfile access.log --error-logfile error.log