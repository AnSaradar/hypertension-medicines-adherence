FROM python:3.9.20

WORKDIR /app/src

COPY requirements.txt /app/src/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

