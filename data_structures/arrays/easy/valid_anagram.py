def anagram(s, t):
    if len(s) != len(t):
        return False
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord("a")] += 1
        count[ord(t[i]) - ord("a")] -= 1
    return max(count) == 0 and min(count) == 0





