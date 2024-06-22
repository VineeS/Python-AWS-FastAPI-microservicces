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
	#build 
deploy:
	#deploy
all: install lint test deploy