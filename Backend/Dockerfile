FROM alpine:3.11

LABEL maintener="Cedric M'Passi"

RUN apk upgrade && apk add python3 python3-dev libcurl curl-dev
RUN mkdir -p /app/data

COPY ./app /app/app
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add build-base mariadb-dev libffi-dev && \
    pip3 install --upgrade pip && pip3 install -r requirements.txt && \
    apk del build-base

RUN pip install remote-pdb pdbpp
EXPOSE 5000

ENV PYTHONUNBUFFERED=1

#ENTRYPOINT ["python"]

CMD [ "./app/app.py" ]
