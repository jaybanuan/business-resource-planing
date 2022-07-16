##############################################################################
# Targets

VERSION := $(shell cat VERSION)

IMAGE_REPO_PREFIX := ""
IMAGE_REPO_BASENAME := $(shell basename $(CURDIR))
IMAGE_REPO := $(IMAGE_REPO_PREFIX)$(IMAGE_REPO_BASENAME):$(VERSION)


##############################################################################
# Targets

.PHONY: clean
clean:
	echo "do nothing."


.PHONY: build
build:
	docker build \
		--tag $(IMAGE_REPO) \
		--no-cache \
		./

.PHONY: test
test:
	pytest tests
