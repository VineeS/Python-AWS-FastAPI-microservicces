install:
	#install commands 
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format test
	black *.py myLib/*.py
lint:
	#check syntax # flake8 and pylint
	pylint --disable=R,C *.py 
test:
	#test 
	python -m pytest -vv --cov=myLib --cov=main test_*.py
build:
	#docker image
	docker build -t deploy-fastapi .
run:
	#run docker
	docker run -p 127.0.0.1:8080:8080 54a0770f9295
deploy:
	#deploy
all: install lint test deploy