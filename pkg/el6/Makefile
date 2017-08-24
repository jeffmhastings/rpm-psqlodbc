image_tag := psqlodbc-rpmbuild-centos6
target_dir := rpms

.PHONY: build
build: image | $(target_dir)
	docker run --rm -v $(shell pwd)/rpms:/rpmbuild/RPMS/x86_64/ ${image_tag}

.PHONY: image
image:
	docker build -t ${image_tag} -f Dockerfile ../..

$(target_dir):
	mkdir -p $(target_dir)

.PHONY: clean
clean:
	-docker rmi ${image_tag}
	-rm -rf rpms
