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

collectstatic:
    uv run python manage.py collectstatic

bootstrap: up prepare_resources collectstatic
    @echo "Done 🚀"
