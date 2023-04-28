FROM python:3.8-slim-buster
ADD . /python-flask
ENV env_name DB_CONNECTION_STRING
WORKDIR /python-flask
RUN pip install -r requirements.txt
CMD ["python", "./app.py"]