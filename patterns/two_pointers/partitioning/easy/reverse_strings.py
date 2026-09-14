def reverse_string(s):
   result = []
   for i in range(len(s)-1, -1, -1):
       result.append(s[i])
   return result

def optimal(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
