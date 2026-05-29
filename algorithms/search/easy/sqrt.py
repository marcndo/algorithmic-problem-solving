def sqrt(x:int) -> int:
    if x <= 1:
        return 1
    l,r = 1, x
    while l <= r:
        m = (l+r) // 2
        val = m * m
        if val == x:
            return m
        elif val < x:
            result = m
            l = m + 1
        else:
            r = m - 1
    return result


x = 17
print(sqrt(17))