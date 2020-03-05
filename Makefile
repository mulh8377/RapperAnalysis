data-mine-local:
	echo fix data-mine-local
	#python3 ...
data-mine-venv:
	echo fix data-mine-venv
	#pipenv run python ...
run-local:
	python3 src/main.py
run-venv:
	pipenv run python src/main.py
test-modules:
	echo fix me
	#pipenv run pytest tests/
