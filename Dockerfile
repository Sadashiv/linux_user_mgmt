#FROM python:3.12.0
FROM python:3.12-slim-bookworm

EXPOSE 8000

# Set Python output is sent straight to terminal to see the output in realtime.
ENV PYTHONUNBUFFERED=1

COPY . /opt
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /opt
RUN pip install -r requirements.txt && rm -rf /var/lib/apt/lists/*
#ENTRYPOINT ['./entrypoint.sh']
#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

