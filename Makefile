
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
	docker build -t entelai-app .
run:
	#run docker
	docker run entelai-app
deploy:
	#deploy
all: install lint test format build run deploy