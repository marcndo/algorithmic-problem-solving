def product_except_self(nums):
    answer = [1]
    for i in range(1, len(nums)):
        answer.append(nums[i-1] * answer[i-1])
    product = 1
    print(product)
    for j in range(len(nums) - 2, -1, -1):
        product *= nums[j+1]
        answer[j] *= product
    return answer
    
print(product_except_self([1, 2, 3, 4, 5, 6]))