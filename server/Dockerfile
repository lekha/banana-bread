FROM python:latest

WORKDIR /server/server

ADD ./media /media

ADD ./server/requirements.txt /server/requirements.txt
RUN pip install -r /server/requirements.txt

ADD ./server /server
RUN pip install -e /server

CMD ["python", "-m", "app"]
