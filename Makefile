# Makefile for MLOps Lab project

.PHONY: help install test lint format clean docker-build docker-test docker-run

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

install:  ## Install dependencies
	pip install -r requirements.txt

install-dev:  ## Install development dependencies
	pip install -e .[dev]

test:  ## Run unit tests
	python -m unittest discover -s . -p "test_*.py" -v

test-coverage:  ## Run tests with coverage
	coverage run -m unittest discover -s . -p "test_*.py" -v
	coverage report -m
	coverage html

lint:  ## Run linting
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format:  ## Format code
	black .
	isort .

security:  ## Run security checks
	bandit -r . -f json -o bandit-report.json
	safety check

clean:  ## Clean up generated files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/

docker-build:  ## Build Docker image
	docker build -t mlops-lab:latest .

docker-test:  ## Run tests in Docker
	docker build --target test -t mlops-lab:test .
	docker run --rm mlops-lab:test

docker-train:  ## Run training stage in Docker
	docker build --target train -t mlops-lab:train .
	docker run --rm mlops-lab:train

docker-build-stage:  ## Run build stage in Docker
	docker build --target build -t mlops-lab:build .
	docker run --rm mlops-lab:build

docker-run:  ## Run Docker container
	docker run --rm -p 8080:8080 mlops-lab:latest

docker-shell:  ## Get shell in Docker container
	docker run --rm -it mlops-lab:latest /bin/bash

all: format lint test  ## Run all checks