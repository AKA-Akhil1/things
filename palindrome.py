def is_palindrome(s):
    """Check if a string is a palindrome."""
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]