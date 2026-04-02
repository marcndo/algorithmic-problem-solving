"""
https://leetcode.com/problems/group-anagrams/description/
"""
from collections import defaultdict

def group_anagram(arr: list[str]):
    anagrams = {}
    for word in arr:
        char_count = [0] * 26
        for char in word:
            char_count[ord(char) - ord("a")] += 1
        key_word = str(char_count)
        if key_word not in anagrams:
            anagrams[key_word] = [word]
        else:
            anagrams[key_word].append(word)
    return list(anagrams.values())


def optimal(arr: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    for word in arr:
        char_count = [0] * 26
        for char in word:
            char_count[ord(char) - ord("a")] += 1
        anagrams[tuple(char_count)].append(word)
    return list(anagrams.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagram(strs))




