run:
	docker compose up --build --remove-orphans

prune:
	docker system prune -f
