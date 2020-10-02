FROM python:3-alpine
RUN apk add --no-cache openssh openrc
WORKDIR /usr/src/app
RUN pip install --no-cache-dir flask

EXPOSE 5000

COPY redfish_server_simulator.py app.py
CMD [ "python", "./app.py" ]
