FROM python:3.12.2-slim


RUN apt-get update \
    && apt install -y postgresql-client cron

RUN pip install poetry==1.7.1

WORKDIR /code

COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --only main


COPY ./source_code /code/source_code

RUN echo "45 23 * * * cd /code && python source_code/scheduler.py >> /var/log/cron.log 2>&1" | crontab
RUN touch /var/log/cron.log

RUN echo "#!/bin/bash\n\
cron\n\
uvicorn source_code.app:app --host 0.0.0.0 --reload" > /code/entrypoint.sh \
&& chmod +x /code/entrypoint.sh

CMD ["/code/entrypoint.sh"]