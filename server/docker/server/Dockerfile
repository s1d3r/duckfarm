FROM python:3.13.0b2-slim

ENV PYTHONPATH=/app:${PYTHONPATH}

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./docker/server/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
