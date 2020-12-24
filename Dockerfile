FROM ubuntu:focal

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get install -y -q tini curl python3 python3-pip

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app

RUN pip3 install --no-cache-dir -r requirements.txt

ADD . /usr/src/app

RUN useradd portcheck

USER portcheck

EXPOSE 8080

ENTRYPOINT ["tini", "--", "gunicorn", "-b0.0.0.0:8080", "portcheck:app", "--workers=5", "--worker-tmp-dir=/dev/shm", "--log-file=-"]
