FROM python:3.7

# Set some environment variables
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app

ENV PORT 8000

# create root directory for our project in the container
RUN mkdir $APP_HOME

# Set the working directory to /app.
WORKDIR $APP_HOME

# Install pipenv
RUN pip install pipenv
RUN pip install uvicorn[standard]

# Copy the current directory contents into the container at /app
COPY Pipfile* ./

# Instal packages
RUN pipenv install --system

#Copy code into app directory
COPY . /app/

EXPOSE $PORT

# Run the gunicorn web server with 1 worker and 8 threads
CMD exec gunicorn --bind :$PORT --workers 2 --threads 8 --timeout 120 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8001 app.main:app
