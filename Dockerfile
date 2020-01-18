FROM python:3.7.2

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/code/api:/code/
ENV PATH=$PATH:/code/config:/code/
ENV PATH=$PATH:/code/libs:/code/
ENV PATH=$PATH:/code/scripts:/code/
ENV PATH=$PATH:/code/scripts:/code/
ENV PYTHONPATH /code

COPY ./pyproject.toml /

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false --local && \
    poetry install

COPY . /

WORKDIR /code