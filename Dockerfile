FROM python:3.7.2

RUN mkdir /code
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/code/api:/code/
ENV PYTHONPATH /code


RUN pip3 install --upgrade pip
RUN pip3 install poetry

COPY . /code/

RUN poetry config virtualenvs.create false --local

RUN poetry install