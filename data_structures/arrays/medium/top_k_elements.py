def top_k(nums):
    count = {}
    for val in nums:
        count[val] = 1 + count.get(val,0)
    arr = []
    for val,freq in count.items():
        arr.append([freq,val])
    arr.sort()
    result = []
    while len(result) < k:
        result.append(arr.pop()[1]) 
    return result


