# Multi-stage Dockerfile for MLOps Lab Project
# Supports train, test, build, and deploy stages

# Base stage with Python and dependencies
FROM python:3.9-slim as base

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Train stage - for data preparation and model training (if applicable)
FROM base as train
LABEL stage=train
CMD ["python", "-c", "print('Training stage - All modules loaded and ready for training workflows')"]

# Test stage - run all unit tests
FROM base as test
LABEL stage=test
RUN python -m unittest discover -s . -p "test_*.py" -v
CMD ["python", "-m", "unittest", "discover", "-s", ".", "-p", "test_*.py", "-v"]

# Build stage - prepare application for deployment
FROM base as build
LABEL stage=build
RUN python -m py_compile *.py
RUN python -c "import factorial, palindrome, prime, ascend, fibo; print('All modules compiled successfully')"
CMD ["python", "-c", "print('Build stage complete - All modules verified and compiled')"]

# Deploy stage - minimal production image
FROM python:3.9-slim as deploy
LABEL stage=deploy

WORKDIR /app

# Copy only necessary files for production
COPY factorial.py palindrome.py prime.py ascend.py fibo.py __init__.py ./
COPY requirements.txt .

# Install only production dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a simple API or CLI interface
COPY <<EOF /app/main.py
#!/usr/bin/env python3
"""
MLOps Lab - Production Entry Point
"""

import sys
from factorial import factorial
from palindrome import is_palindrome
from prime import is_prime
from ascend import sort_ascending
from fibo import fibonacci_sequence

def main():
    print("MLOps Lab - Mathematical Functions API")
    print("Available functions:")
    print("- factorial(n)")
    print("- is_palindrome(s)")
    print("- is_prime(n)")
    print("- sort_ascending(lst)")
    print("- fibonacci_sequence(n)")
    
    # Example usage
    print(f"\\nExample: factorial(5) = {factorial(5)}")
    print(f"Example: is_palindrome('racecar') = {is_palindrome('racecar')}")
    print(f"Example: is_prime(17) = {is_prime(17)}")
    print(f"Example: sort_ascending([3,1,4,2]) = {sort_ascending([3,1,4,2])}")
    print(f"Example: fibonacci_sequence(10) = {fibonacci_sequence(10)}")

if __name__ == "__main__":
    main()
EOF

RUN chmod +x /app/main.py

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import factorial, palindrome, prime, ascend, fibo" || exit 1

EXPOSE 8080

CMD ["python", "main.py"]

# Default stage
FROM deploy as default