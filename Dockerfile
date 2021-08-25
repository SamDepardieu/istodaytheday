FROM python:3.8-alpine

EXPOSE 5000/tcp

WORKDIR /app

COPY requirements.txt .
COPY templates ./templates
COPY static/ ./static

RUN pip install -r requirements.txt

COPY app.py .

CMD ["gunicorn", "app:app", "--bind=0.0.0.0:5000"]
