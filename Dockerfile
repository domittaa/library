FROM python:3.12.2-slim


RUN apt-get update \
    && apt install -y postgresql-client

RUN pip install poetry==1.7.1

WORKDIR /code

COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --only main


COPY ./source_code /code/source_code

CMD ["bash", "-c", "uvicorn source_code.app:app --host 0.0.0.0 --reload"]