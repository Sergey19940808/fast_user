FROM python:3.7.2

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH /code

COPY ./pyproject.toml /

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false --local && \
    poetry install

WORKDIR /code

COPY . /code/