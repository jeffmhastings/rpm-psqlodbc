image_tag := psqlodbc-rpmbuild-centos6

.PHONY: rpms
rpms: image
	docker run --rm -it -v $(shell pwd)/rpms:/rpmbuild/RPMS/x86_64/ ${image_tag}

.PHONY: image
image:
	docker build -t ${image_tag} -f Dockerfile ../..

.PHONY: clean
clean:
	docker rmi ${image_tag}
	rm -rf rpms
