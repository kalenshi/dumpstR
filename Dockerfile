FROM python:3.11

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# create the working directory
RUN mkdir -p /dumpstr

# switch to the working directory
WORKDIR /dumpstr
COPY . .

#Upgrade pip and install requirements
RUN pip install --upgrade pip && \
    pip install -r ./requirements.txt

# Copy all the required files into the image
