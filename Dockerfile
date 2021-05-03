FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# Adding backend directory to make absolute filepaths consistent across services
WORKDIR /app/backend

# Install Python dependencies

RUN apt-get update
COPY requirements.txt /app/backend
RUN pip install -r requirements.txt

# Add the rest of the code
COPY . /app/backend/

# # Make port 8000 available for the app
# EXPOSE 8000

# # Be sure to use 0.0.0.0 for the host within the Docker container,
# # otherwise the browser won't be able to find it
# CMD python manage.py runserver 0.0.0.0:8000