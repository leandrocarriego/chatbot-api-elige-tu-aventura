IMAGE_NAME=entelai-app
CONTAINER_NAME=entelai-container

install:
	#install dependencies
	pip install --upgrade pip &&\
	pip install -r requirements.txt
lint:
	#lint
test:
	#test
format:
	#format
build:
	#build container
	docker-compose build
run:
	#run docker
	docker-compose up -d
test-container:
	#test container
	sleep 10
	curl --fail http://localhost:5000/ || exit 1
clean:
	docker-compose down
deploy:
	#deploy
all: install lint test format build run deploy