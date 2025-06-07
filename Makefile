PROJECT_ID := 'kartoza_geonode'
SHELL := /bin/bash

rebuild:
	@docker-compose build ${EXTRA_ARGS} django
	@docker-compose build ${EXTRA_ARGS}

reload:
	@docker-compose exec django touch /tmp/django.pid

up:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose up -d

down:
	@docker-compose down

kill:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Killing in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose kill

rm: kill
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Removing production instance!!! "
	@echo "------------------------------------------------------------------"
	@docker-compose rm

rm-volumes:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Removing all volumes!!!! "
	@echo "------------------------------------------------------------------"
	@docker volume ls -q | grep '^kartoza_geonode' | xargs -r docker volume rm