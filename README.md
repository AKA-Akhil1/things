# MLOps Lab Project

This project contains various mathematical utility functions with comprehensive test coverage and CI/CD pipeline.

## Modules

- `factorial.py` - Calculate factorial of numbers
- `palindrome.py` - Check if strings are palindromes
- `prime.py` - Check if numbers are prime
- `ascend.py` - Sort lists in ascending order
- `fibo.py` - Generate Fibonacci sequences

## Testing

Run all tests:
```bash
python -m unittest discover -s . -p "test_*.py"
```

Run specific test:
```bash
python -m unittest test_factorial.py
```

## Docker

Build the image:
```bash
docker build -t mlops-lab .
```

Run tests in container:
```bash
docker run --rm mlops-lab test
```

## CI/CD

This project uses GitHub Actions for automated testing and deployment. The pipeline runs on every push and pull request.

## Requirements

- Python 3.9+
- unittest (built-in)