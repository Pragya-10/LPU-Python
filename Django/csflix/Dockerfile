FROM python:3.9-slim

RUN pip install poetry gunicorn

COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY . .

ENTRYPOINT [ "gunicorn", "csflix.wsgi", "-b", "0.0.0.0:8000" ]
