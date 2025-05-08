set dotenv-load

default:
    just --list

up:
    docker compose up -d

down:
    docker compose down

alias m := manage

manage +args:
    uv run python manage.py {{args}}

prepare_resources:
    uv run python manage.py bootstrap_s3
    uv run python manage.py bootstrap_sqs
    uv run python manage.py bootstrap_lambda

collectstatic:
    uv run python manage.py collectstatic

bootstrap: up prepare_resources collectstatic
    @echo "Done 🚀"

# Celery commands
celery_worker:
    uv run celery -A localstack_demo worker -l info
