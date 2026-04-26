"3.Longest Substring Without Repeating Characters"

def longest_substring(s):
    char = set()
    j = 0
    max_length = 0
    for i in range(len(s)):
        while s[i] in char:
            char.remove(s[j])
            j += 1
        char.add(s[i])
        max_length = max(max_length, i - j + 1)
    return max_length


s = "abcabcbb"

print(longest_substring(s))


