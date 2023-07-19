FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /deamon
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./ ./
CMD [ "python", "pubsub/test.py"]

