def max_water_quantity(height):
    max_quantity = 0
    l, r = 0, len(height) - 1
    while l < r:
        area = min(height[l], height[r]) * (r-l)
        max_quantity = max(max_quantity, area)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return max_quantity