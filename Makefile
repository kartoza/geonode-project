PROJECT_ID := 'gep'
SHELL := /bin/bash

rebuild:
	@docker-compose build ${EXTRA_ARGS} django
	@docker-compose build ${EXTRA_ARGS} dev
	@docker-compose build ${EXTRA_ARGS}

reload:
	@docker-compose exec django touch /tmp/django.pid

build-up:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose up -d db
	@docker-compose up -d frontend
	@docker-compose up -d backend
	@make prepare-dev-db
	@make up

up:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose up -d

frontend-up:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "up frontend"
	@echo "------------------------------------------------------------------"
	@docker-compose up -d frontend

frontend-build:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "prepare database"
	@echo "------------------------------------------------------------------"
	@docker-compose exec frontend yarn build

backend-up:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "up frontend"
	@echo "------------------------------------------------------------------"
	@docker-compose up -d backend

dev-up:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "up frontend"
	@echo "------------------------------------------------------------------"
	@docker-compose up -d dev

geonode-up:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in production mode"
	@echo "------------------------------------------------------------------"
	@cd geonode/scripts/spcgeonode; docker-compose up --build -d django geoserver postgres nginx

prepare-dev-db:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "prepare database"
	@echo "------------------------------------------------------------------"
	@docker-compose exec backend npm run prepare-dev-db

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
	@docker volume rm $(PROJECT_ID)_certificates $(PROJECT_ID)_database $(PROJECT_ID)_geodatadir $(PROJECT_ID)_pgdumps $(PROJECT_ID)_rabbitmq $(PROJECT_ID)_gep-database
	@docker volume rm $(PROJECT_ID)_osm-postgis-data $(PROJECT_ID)_import_queue $(PROJECT_ID)_import_done $(PROJECT_ID)_cache