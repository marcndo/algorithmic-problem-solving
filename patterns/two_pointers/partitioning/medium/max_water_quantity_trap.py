def max_water_quantity(height):
    max_quantity = 0
    n = len(height)
    for i in range(n):
        for j in range(i+1,n):
            curr_quantity = min(height[i], height[j]) * (j-i)
            max_quantity = max(max_quantity, curr_quantity)
    return max_quantity

def optimal(height):
    l, r = 0, len(height)-1
    max_quantity = 0
    while l < r:
        curr_quantity = min(height[l], height[r]) * (r - l)
        max_quantity = max(max_quantity, curr_quantity)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_quantity

