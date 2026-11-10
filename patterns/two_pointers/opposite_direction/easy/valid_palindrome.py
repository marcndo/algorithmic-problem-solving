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


def optimal(s):
    s = s.lower()
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def opt(s):
    s = s.lower()
    stak = []
    for ch in s:
        if ch.isalnum():
            stak.append(ch)
    for ch in s:
        if ch.isalnum():
            if ch != stak.pop():
                return False
    return True


s = "Was it a car or a cat I saw?"
print(is_valid_palindrom(s))
print(optimal(s))