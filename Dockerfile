FROM ubuntu:latest

ENV http_proxy http://165.225.104.34:10015
ENV https_proxy http://165.225.104.34:10015

EXPOSE 5000
EXPOSE 9001

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip 
RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_11.x  | bash -
RUN apt-get -y install nodejs
RUN npm i frontail -g

COPY requirements.txt /app/requirements.txt

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "flasklogreader.py"]
