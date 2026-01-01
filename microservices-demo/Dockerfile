FROM python:alpine3.18
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY monolith.py .
EXPOSE 5000
CMD ["python", "monolith.py"]