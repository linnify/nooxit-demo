FROM python:3.8

# Set some environment variables
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app

ENV PORT 8001

# create root directory for our project in the container
RUN mkdir $APP_HOME

# Set the working directory to /app.
WORKDIR $APP_HOME

# Install peotry
RUN pip install poetry
RUN pip install uvicorn[standard]

# Copy the current directory contents into the container at /app
COPY poetry.lock pyproject.toml $APP_HOME/

# Instal packages
# Create a false virtual env and then install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

#Copy code into app directory
COPY . /app/

EXPOSE $PORT

# Run the gunicorn web server with 1 worker and 8 threads
CMD exec gunicorn --bind :$PORT --workers 2 --threads 8 --timeout 120 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 app.main:app
