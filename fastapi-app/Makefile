APP_NAME=fastapi-app
K8S_DIR=./k8s

# Generate TAG only once per make execution
TAG := $(shell date +%Y%m%d%H%M%S)

build:
	docker build -t $(APP_NAME):$(TAG) .

load:
	minikube image load $(APP_NAME):$(TAG)

deploy:
	kubectl set image deployment/fastapi-deployment fastapi-container=$(APP_NAME):$(TAG)

rollout:
	kubectl rollout status deployment/fastapi-deployment

all: build load deploy rollout

clean:
	minikube ssh "docker image prune -f"

