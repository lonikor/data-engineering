FROM python:3.12-rc-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3", "app.py"]