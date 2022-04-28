FROM python:3.10.1-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT=prod
ENV TESTING=1

RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

RUN pip install --upgrade pip --index-url https://mirrors.aliyun.com/pypi/simple/
COPY ./requirements.txt .
RUN pip install -r requirements.txt --index-url https://mirrors.aliyun.com/pypi/simple/

COPY . .

CMD [ "uvicorn", "app.main:app","--reload", "--host", "0.0.0.0" ]