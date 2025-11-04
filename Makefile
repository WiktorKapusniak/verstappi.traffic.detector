DOCKER_USER=underwoodsteam
IMAGE=$(DEPLOYMENT)-$(END)

build:
	@docker build -t $(DOCKER_USER)/$(IMAGE):latest $(END)/
	@echo $(DOCKER_TOKEN) | docker login -u $(DOCKER_USER) --password-stdin
	@docker push $(DOCKER_USER)/$(IMAGE):latest
