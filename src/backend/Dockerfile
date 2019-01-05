# TODO: Setup with gunicorn

FROM python:3.7.2-slim

RUN mkdir /app
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
RUN ls
CMD ["python", "/app/application.py"]