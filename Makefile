.PHONY: check test

check:
	./scripts/check_todo_format.sh
	python3 -m pytest

test: check
