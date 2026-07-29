.PHONY: check test clean stats

check:
	./scripts/check_todo_format.sh
	python3 -m pytest

test: check

stats:
	python3 scripts/todo_stats.py

clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	rm -rf .pytest_cache
