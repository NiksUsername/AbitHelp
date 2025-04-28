FROM python:3.12-slim

RUN mkdir /app

RUN apt update && \
    apt install -y libpq-dev gcc

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD [ "sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000" ]
