def max_profit(nums):
    max_p = 0
    j = 0
    for i in range(1,len(nums)):
        if prices[j] <= prices[i]:
            max_p = max(max_p, prices[i]-prices[j])
        else:
            j = i
    return max_p