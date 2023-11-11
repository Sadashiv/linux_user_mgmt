FROM python:3.12.0

EXPOSE 8000

# Set Python output is sent straight to terminal to see the output in realtime.
ENV PYTHONUNBUFFERED=1

COPY . /opt
WORKDIR /opt
RUN pip install -r requirements.txt
#ENTRYPOINT ['./entrypoint.sh']
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
