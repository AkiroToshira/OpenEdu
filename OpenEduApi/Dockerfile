FROM python:3.8.5-alpine

RUN pip install --upgrade pip

COPY requirements.txt .

RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow

RUN pip install -r requirements.txt

COPY ./OpenEduApi /app

WORKDIR /app

COPY entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]