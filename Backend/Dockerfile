FROM alpine:3.10

LABEL maintener="Cedric M'Passi"

RUN apk upgrade && apk add python3 python3-dev py-pip

COPY ./app /app/app
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

#ENTRYPOINT ["python"]

CMD [ "./app/app.py" ]
