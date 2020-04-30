FROM ubuntu:18.04

LABEL maintener="Cedric M'Passi"

RUN apt-get update -y && apt-get install -y python-pip python-dev

COPY ./app /app/app
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

#ENTRYPOINT ["python"]

CMD [ "./app/app.py" ]
