FROM python:3.11-slim
WORKDIR /app
RUN pip install requests
COPY . .
CMD ["python3", "worker.py"]
