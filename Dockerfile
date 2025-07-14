FROM python:3.11-slim-buster

WORKDIR /app

COPY requc.txt .

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requc.txt

COPY bot.py .

CMD ["python3", "bot.py"]
