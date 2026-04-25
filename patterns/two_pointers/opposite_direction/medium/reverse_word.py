"151. Reverse Words in a String"
def reverse_word(s):
    s = s.split()
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            continue
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return " ".join(s)


s = "         them  sky is         blue"
print(reverse_word(s))

