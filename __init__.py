"""
MLOps Lab Package
Mathematical utility functions with test coverage
"""

__version__ = "1.0.0"
__author__ = "MLOps Lab"

from .factorial import factorial
from .palindrome import is_palindrome
from .prime import is_prime
from .ascend import sort_ascending
from .fibo import fibonacci_sequence

__all__ = [
    'factorial',
    'is_palindrome',
    'is_prime',
    'sort_ascending',
    'fibonacci_sequence'
]