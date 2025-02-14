IMAGE_NAME = python:3.13.2-alpine3.21
CONTAINER_NAME = relaxed_euler

SERVICE = django
COMPOSE = docker-compose

run:
	sudo docker run -d -p 8000:8000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

stop:
	sudo docker stop $(CONTAINER_NAME) || true
	sudo docker rm $(CONTAINER_NAME) || true

up:
	sudo $(COMPOSE) up -d

down: 
	sudo $(COMPOSE) down

ps: 
	sudo docker ps

test:
	python main.py