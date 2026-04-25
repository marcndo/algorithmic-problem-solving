"344. Reverse String"

def reverse_string(s):
    left, right = 0, len(s) - 1
    if len(s) < 2:
        return s
    while left < right:
        if s[left] == s[right]:
            continue
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

s = ["h","e","l","l","o"]

print(reverse_string(s))