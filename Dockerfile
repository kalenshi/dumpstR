FROM python:3.11

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

USER root
# create the working directory
RUN apt-get update && \
    apt-get  install -y libpq-dev gcc && \
    pip install --upgrade pip && \
    pip install psycopg2

RUN mkdir  /app

# switch to the working directory
WORKDIR /app
RUN useradd -m dumpstr && \
    chown -R dumpstr:dumpstr /app



COPY requirements.txt requirements.txt

#Upgrade pip and install requirements
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
