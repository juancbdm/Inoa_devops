FROM python:3.11.0-alpine3.16
RUN apk add --no-cache --virtual .build-deps \
    postgresql-libs \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev
WORKDIR /inoa_python_app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt 
EXPOSE 80
CMD ["python3","./src/app.py"]