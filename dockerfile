FROM python:3.8.2-alpine3.11
LABEL author="akashK" 
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD [ "gunicorn","app:app"] 

