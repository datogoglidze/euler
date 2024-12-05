amend:
	git commit --amend --no-edit -a

install:
	python -m pip install --upgrade pip
	python -m pip install --upgrade poetry
	poetry install

lock:
	poetry lock --no-update

update: install
	poetry update

format:
	poetry run ruff format problems tests
	poetry run ruff check  problems tests --fix

lint:
	poetry run ruff format problems tests --check
	poetry run ruff check problems tests
	poetry run mypy problems tests

test:
	poetry run pytest tests \
		--last-failed \
		--cov
