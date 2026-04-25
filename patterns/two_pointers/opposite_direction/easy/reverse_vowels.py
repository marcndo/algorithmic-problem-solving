"345. Reverse Vowels of a String"

def reverse_vowels(s):
    vowels = {"a", "e","i", "o", "u", "A", "E", "I", "O", "U"}
    left, right = 0, len(s) - 1
    s = list(s)
    while left < right:
        if s[left] == s[right]:
            continue
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)


