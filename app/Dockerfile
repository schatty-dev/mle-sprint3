FROM python:3.11-slim

COPY . ./churn_app

WORKDIR simple_fast_api 

RUN pip3 install -r requirements.txt

EXPOSE 8081

CMD uvicorn churn_app:app --host 0.0.0.0 --port 8081