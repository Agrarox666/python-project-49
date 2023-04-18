install:
	poetry install
package-install:
	python3 -m pip install --user dist/*.whl
force-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl
build:
	poetry build
publish:
	poetry publish --dry-run
brain-games:
	poetry run brain-games
linter:
	poetry run flake8 brain_games
