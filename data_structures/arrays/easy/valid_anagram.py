"""https://leetcode.com/problems/valid-anagram/description/
Anagram: string form by rearranging the letters of a different string
"""

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    char_freq = [0] * 26
    for i in range(len(s)):
        char_freq[ord(s[i]) - ord("a")] += 1
        char_freq[ord(t[i]) - ord("a")] -= 1
    return min(char_freq) == 0 and max(char_freq) == 0





