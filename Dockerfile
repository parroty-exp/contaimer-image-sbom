FROM python:3-slim
COPY ./src /app
COPY ./requirements.txt /app

WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "server.py"]
