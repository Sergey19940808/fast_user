# Main image
FROM python:3.7.2

# Create dir of project
RUN mkdir /code
WORKDIR /code

# Set envs vars
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/code/api:/code/
ENV PYTHONPATH /code

# Install all the requirements
RUN pip3 install --upgrade pip
RUN pip3 install poetry

# Copy code in the dir of project
COPY . /code/

# Set stop to create venv
RUN poetry config virtualenvs.create false --local

# Install all packages
RUN poetry install