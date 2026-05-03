# j determins end of the 

def drop_adj_duplicates(s):
    arr = list(s)
    j = 0
    for i in range(len(s)):
        arr[j] = arr[i]
        if j > 0 and arr[j] == arr[j-1]:
            j -= 1
        else:
            j += 1
    return "".join(arr[:j])
    

s = "abbaca"
print(drop_adj_duplicates(s))