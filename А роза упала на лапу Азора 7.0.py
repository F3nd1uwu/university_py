def is_palindrome(x):
    if isinstance(x, int):
        x = str(x)
    if isinstance(x, (str, list, tuple)):
        items = list(x)
        return items == items[::-1]
    return False

    
print(is_palindrome(12321))