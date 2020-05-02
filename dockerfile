FROM python:3.8.2
MAINTAINER "Akashdeep Kashyap"

COPY . /app
WORKDIR /app



RUN pip3 install -r requirements.txt


EXPOSE 5001 
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 