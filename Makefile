# Makefile for managing Docker Compose

# Phony targets
.PHONY: up down build logs clean

# Bring up the services
up:
	docker-compose up -d

# Bring down the services
down:
	docker-compose down

# Build the services
build:
	docker-compose build

# View logs
logs:
	docker-compose logs -f

# Clean up all containers, images, and volumes
clean:
	docker-compose down --volumes --remove-orphans
	docker system prune -f --volumes
