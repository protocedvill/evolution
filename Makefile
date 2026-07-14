.PHONY: check test clean

check:
	./scripts/check_todo_format.sh
	python3 -m pytest

test: check

clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	rm -rf .pytest_cache
