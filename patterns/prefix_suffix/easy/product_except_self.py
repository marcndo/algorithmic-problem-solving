def product_except_self(nums):
    answer = []
    n = len(nums)
    for i in range(n):
        prod = 1
        for j in range(n):
            if i == j:
                continue
            prod *= nums[j]
        answer.append(prod)
    return answer

def optimal(nums):
    n = len(nums)
    answer = [1]
    for i in range(1, n):
        answer.append(answer[i-1]*nums[i-1])
    prod = 1
    for j in range(n-1,-1,-1):
        answer[j] *= prod
        prod *= nums[j]
    return answer