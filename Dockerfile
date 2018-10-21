FROM python:alpine3.8

RUN pip install boto3

ADD app.py /app.py

ENTRYPOINT python /app.py
