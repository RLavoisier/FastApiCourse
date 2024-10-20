.PHONY: runserver

runserver:
	uvicorn books:app --reload

.PHONY: format
format:
	pre-commit run --all-files
