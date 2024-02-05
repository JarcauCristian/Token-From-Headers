FROM python:3.11-slim

WORKDIR /usr/src/app

COPY main.py .
COPY redis_cache.py .

RUN pip install redis streamlit

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]