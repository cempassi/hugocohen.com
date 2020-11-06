FROM alpine:3.11

LABEL maintener="Cedric M'Passi"

RUN apk upgrade && apk add bash python3 python3-dev libcurl curl-dev
RUN mkdir -p /app/data

COPY ./requirements.txt /app/requirements.txt
COPY ./wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

WORKDIR /app

RUN apk add tiff-dev build-base mariadb-dev libffi-dev git libjpeg-turbo-dev zlib-dev && \
    pip3 install --upgrade pip && pip3 install -r requirements.txt && \
    apk del build-base git

RUN pip install remote-pdb pdbpp

COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod 777 /app/entrypoint.sh
COPY ./app /app/app
EXPOSE 5000

ENV PYTHONUNBUFFERED=1

#ENTRYPOINT ["python"]

#CMD [ "./app/app.py" ]
