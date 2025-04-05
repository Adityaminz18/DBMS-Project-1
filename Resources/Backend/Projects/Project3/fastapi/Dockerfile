FROM python:3.13.2

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 80:8000

CMD uvicorn main:app --reload --port=8000 --host=0.0.0.0

