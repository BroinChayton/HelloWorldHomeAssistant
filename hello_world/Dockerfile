FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY run.sh ./run.sh
COPY main.py ./main.py

RUN chmod a+x run.sh
CMD ["/app/run.sh"]
