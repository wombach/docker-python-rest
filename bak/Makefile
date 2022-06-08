include ./python_rest_env

build:
	@docker build -t nxtgen.azurecr.io/$(repository):$(version) .
run:
	docker run -p 8080:8080 --name $(repository) --env ES_INDEX="eis--public--equipment--flattened" --env ES_URL="https://nxtgen-dev.es.westeurope.azure.elastic-cloud.com:9243/" nxtgen.azurecr.io/$(repository):$(version)
kill:
	@echo 'Killing container...'
	@docker ps | grep $(repository) | awk '{print $$1}' | xargs docker rm -f
info:
	@echo nxtgen.azurecr.io/$(repository):$(version)
