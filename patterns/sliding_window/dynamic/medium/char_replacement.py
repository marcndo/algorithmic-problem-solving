"Leetcode: 424. Longest Repeating Character Replacement"

def repeated_char_replacement(s, k):
    freq_map = {}
    j = 0
    result = 0
    max_freq = 0
    for i in range(len(s)):
        freq_map[s[i]] = freq_map.get(s[i], 0) + 1
        max_freq = max(max_freq, freq_map[s[i]])
        while (i - j + 1) - max_freq > k:
            freq_map[s[j]] -= 1
            j += 1
        result = max(result, i - j + 1)
 
    return result

s = "AABABBA"
s = "ABAB"
s = "AABABBA"
k = 1
print(repeated_char_replacement(s, k))
        