def sort_ascending(lst):
    """Sort a list of integers in ascending order."""
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    for item in lst:
        if not isinstance(item, int):
            raise ValueError("All elements must be integers")
    return sorted(lst)