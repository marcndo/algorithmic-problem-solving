"557. Reverse Words in a String III"

def reverse_word(s):
    words = s.split()
    result = ""
    for word in words:
        i, j = 0, len(word) - 1
        word = list(word)
        while i <= j:
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1
        result = result + " " + "".join(word)
    return result
s = "Let's take LeetCode contest"
s = "Mr Ding"
print(reverse_word(s))
