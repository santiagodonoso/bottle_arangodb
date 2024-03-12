FROM python:3.11.5
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD python -m bottle --server paste --bind 0.0.0.0:80 --debug --reload app