DOCKER_USER=underwoodsteam
IMAGE=$(DEPLOYMENT)-$(END)

build:
	docker build -t $(DOCKER_USER)/$(IMAGE):latest $(END)/
	docker login -u $(DOCKER_USER) -p $(DOCKER_TOKEN)
	docker push $(DOCKER_USER)/$(IMAGE):latest
