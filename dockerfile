FROM python:3.8.2-alpine3.11
MAINTAINER "Akashdeep Kashyap"

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD [ "python3","app.py"] 
