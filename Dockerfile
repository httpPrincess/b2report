FROM debian:wheezy
MAINTAINER jj
ENV PYTHONUNBUFFERED 1
RUN DBEIAN_FRONTEND=noninteractive apt-get update && apt-get install python python-pip -y && \
   apt-get clean autoclean && apt-get autoremove && \
   rm -rf /var/lib/{apt,dpkg,cache,log}
RUN mkdir /app
ADD requirements.txt /app/
RUN cd /app/ && pip install -r requirements.txt && pip install gunicorn
ADD . /app/
ENV LC_CTYPE  en_US.utf-8
EXPOSE 8080
RUN cd /app/ && ./initialize_app.py
VOLUME /app/myapp/data/
VOLUME /app/uploads/
WORKDIR /app/
CMD gunicorn -w 1 -b 0.0.0.0:8080  webapp:app
