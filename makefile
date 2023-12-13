# Makefile

# Variables
MANAGE = docker compose -f local.yml run --rm django python manage.py

# Commands
up:
	docker compose -f local.yml up

up-build:
	docker compose -f local.yml up --build

down:
	docker compose -f local.yml down

down-v:
	docker compose -f local.yml down -v

migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

test:
	docker-compose -f local.yml run --rm django coverage run -m pytest

shell:
	$(MANAGE) shell_plus

superuser:
	$(MANAGE) createsuperuser

precommit:
	pre-commit run --all-files

show:
	docker compose -f local.yml ps

stop-django:
	docker rm -f autobus_local_django

start-django:
	docker-compose -f local.yml run --rm --service-ports django

clean-up:
	docker-compose -f local.yml stop django
	docker-compose -f local.yml run --rm --service-ports django

flush:
	$(MANAGE) flush

users:
	$(MANAGE) create_local_user_and_admin

postgres:
	docker-compose -f local.yml exec postgres psql -U postgres -h postgres -p 5432 autobus

.PHONY: run migrate test shell superuser
