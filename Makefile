#Import environment variables
include .env
export $(shell sed 's/=.*//' .env)

#Terraform variable generation 
include $(shell awk -F= '{print "TF_VAR_"tolower($$1) "="$$2 }' < .env > .tf.env && echo .tf.env)
export $(shell sed 's/=.*//' .tf.env)

REPO 				= cempassi
# Valid workspaces: dev or prod
workspace 	= dev

FRONT_IMAGE = $(REPO)/vimeo-app-frontend
BACK_IMAGE 	= $(REPO)/vimeo-app-backend

all: build

build: build.front build.back

deploy: deploy.front deploy.back

update: deploy
	ssh root@'api.hugocohen.com' 'cd site_hugo; ./refresh.sh'

refresh: 
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
	cd ./infra && terraform workspace new $(workspace)

infra.init:
	cd ./infra && terraform workspace select $(workspace) && terraform init

infra.plan:
	cd ./infra && terraform plan

infra.apply:
	cd ./infra && terraform apply -auto-approve

infra.destroy:
	cd ./infra && terraform destroy -auto-approve

clean:
	docker rmi $(BACK_IMAGE) $(FRONT_IMAGE)
	rm -rf .tf.env

test: 
	env

.SILENT:
