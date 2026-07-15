"567. Permutation in String"
from collections import Counter

def permutation_string(s1, s2):
    if len(s1) > len(s2):
        return False
    s1_count = Counter(s1)
    window_count = s1_count
    j = 0
    for i in range(len(s2)):
        window_count[s2[i]] += 1
        if i - j + 1 > len(s1):
            window_count[s2[j]] -= 1
            if window_count[s2[j]] == 0:
                del window_count[s2[j]]
            j += 1

        if i - j + 1 == len(s1):
            if window_count == s1_count:
                return True
    return False



s1 = "ab"
s2 = "eidb000aoo"
print(permutation_string(s1, s2))

