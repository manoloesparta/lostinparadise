FROM python:3.9-slim

WORKDIR /usr/src/auth

COPY ./requirements.txt /usr/src/auth/requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src/auth

CMD [ "python", "main.py" ]