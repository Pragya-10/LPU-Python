FROM python:3.9-slim

RUN pip install poetry gunicorn

WORKDIR /app

COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY . .

CMD gunicorn csflix.wsgi --bind 0.0.0.0:$PORT
