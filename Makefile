IMAGE_NAME=entelai-app
CONTAINER_NAME=entelai-container

.PHONY: all test

install:
	#install dependencies
	pip install --upgrade pip &&\
	pip install -r requirements.txt
lint:
	#lint
test:
	pytest
format:
	#format
build:
	#build container
	docker build -t entelai-api .
run:
	#run docker
	docker run --name entelai-app -d -p 5000:5000 entelai-api
test-container:
	#test container
	sleep 10
	curl --fail http://localhost:5000/api/v1/ || exit 1
clean:
	docker rm -f entelai-app || true
deploy:
	#deploy
all: install lint test format build run deploy