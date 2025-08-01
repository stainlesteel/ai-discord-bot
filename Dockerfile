FROM python:3.11-slim-buster

WORKDIR /app

COPY . . 

RUN pip install --no-cache-dir -r requc.txt


CMD ["python3", "bot.py"]
