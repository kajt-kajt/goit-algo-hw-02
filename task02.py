from collections import deque
from re import sub

def is_palindrome(line: str) -> bool:
    """
    Function returns True if line provided is palindrome
    """
    # removing all punctuation symbols, whitespaces etc.
    # modifying all characters to lower case and unifying some special letters
    line_sanitized = sub(r"[^\w]|_", "", line.casefold())
    q = deque(line_sanitized)
    while len(q)>1:
        letter1 = q.pop()
        letter2 = q.popleft()
        if letter1 != letter2:
            return False
    return True

print(is_palindrome("І що сало? Ласощі..."))
