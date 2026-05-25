import re

def is_valid_palindrom(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]","",s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


s = "Was it a car or a cat I saw?"
print(is_valid_palindrom(s))