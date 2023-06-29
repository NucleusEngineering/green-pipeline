FROM python:3.9-alpine
WORKDIR /service
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
EXPOSE 8080
ENTRYPOINT ["python3", "main.py"]
