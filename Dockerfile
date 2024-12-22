FROM python:3.12-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

# Configurar a chave API do google
ENV GOOGLE_API_KEY="AIzaSyDBxkNd77mrygNI7orDEGymfUKl6rk2p1A"