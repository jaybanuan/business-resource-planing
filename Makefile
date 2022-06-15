##############################################################################
# Targets

VERSION := $(shell cat VERSION)


##############################################################################
# Targets

.PHONY: clean
clean:
	echo "do nothing."


.PHONY: venv
venv:
	python3 -m venv .venv


.PHONY: pip
pip:
	find . -name requirements.txt | xargs -I{} python3 -m pip install -r {}


.PHONY: build
build:
	$(MAKE) -C brp-api-server build
	$(MAKE) -C brp-web-app build


.PHONY: up
up:
	docker compose up -d


.PHONY: down
down:
	docker compose down


.PHONY: init
init:
	curl http://localhost:8080/init


.PHONY: logs
logs:
	docker compose logs brp-api-server
