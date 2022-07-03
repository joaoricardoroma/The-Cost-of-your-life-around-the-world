up:
	docker-compose up --build

down:
	docker-compose down

build:
	docker exec application pip install -r requirements.txt
	docker exec application python3 manage.py migrate

run:
	docker exec -it application $(command)

user:
	docker exec -it application python3 manage.py createsuperuser
