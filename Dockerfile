FROM python:3.7.2
LABEL maintainer="andreas.wombacher@aureliusenterprise.com"

RUN pip install pipenv

ADD . /rest-services
WORKDIR /rest-services

RUN pipenv install --system --skip-lock

RUN pip install gunicorn[gevent]

# RUN git clone https://github.com/aureliusenterprise/m4i_atlas_core.git
# RUN cd m4i_atlas_core \
#     pip install .

EXPOSE 5000

CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:8080 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level debug
#CMD gunicorn wsgi:app -w 8 --threads 2 -b 0.0.0.0:8080 --max-requests 10000 --timeout 5 --keep-alive 5 --log-level debug