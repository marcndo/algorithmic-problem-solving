"2000. Reverse Prefix of Word"

def reverse_prefix(s, ch):
    idx = s.index(ch)
    left, right = 0, idx
    end_str = s[idx+1:]
    s = list(s[:idx+1])
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    s = "".join(s)
    return s + end_str


word = "abcdefd"
ch = "d"
word = "xyxzxe"
ch = "z"
print(reverse_prefix(word, ch))
