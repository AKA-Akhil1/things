def fibonacci_sequence(n):
    """Generate fibonacci sequence up to n."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    while True:
        next_fib = sequence[-1] + sequence[-2]
        if next_fib > n:
            break
        sequence.append(next_fib)
    return sequence