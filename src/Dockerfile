FROM python:3.7.2-slim

WORKDIR /app
COPY . .

RUN python -m pip install -r requirements.txt

EXPOSE 8000
CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0", "theroast_backend.wsgi" ]