docker-run:
	@docker run -p 8888:8888 -p 4040:4040 -p 4041:4041 -v $(PWD):/home/jovyan/work {{ cookiecutter.docker_image }}
run:
	@python3 setup.py sdist bdist_wheel
	@sh deploy.sh

test:
	@sh test.sh