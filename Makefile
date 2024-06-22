install:
	#install commands 
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format test
	black *.py
lint:
	#check syntax # flake8 and pylint
	pylint --disable=R,C hello.py
test:
	#test 
	python -m pytest -vv test_hello.py
deploy:
	#deploy
all: install lint test deploy