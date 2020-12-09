REPO 				= cempassi
WORKSPACE 	= dev
FRONT_IMAGE = $(REPO)/vimeo-app-frontend
BACK_IMAGE 	= $(REPO)/vimeo-app-backend

all: build

build: build.front build.back

deploy: deploy.front deploy.back

update: deploy
	ssh root@'api.hugocohen.com' 'cd site_hugo; ./refresh.sh'

deploy.back: build.back
	docker push $(BACK_IMAGE)

deploy.front: build.front
	docker push $(FRONT_IMAGE)

build.front:
	$(MAKE) -C Frontend
	docker build -t $(FRONT_IMAGE) ./Frontend 

build.back:
	docker build -t $(BACK_IMAGE) ./Backend

infra.create-workspace:
	cd ./infra && terraform workspace new $(WORKSPACE)

infra.init:
	cd ./infra && terraform workspace select $(WORKSPACE) && terraform init

clean:
	docker rmi $(BACK_IMAGE) $(FRONT_IMAGE)

.SILENT:
