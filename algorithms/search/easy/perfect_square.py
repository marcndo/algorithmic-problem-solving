def is_perfect_square(x:int) -> bool:
    l, r = 0, x
    while l <= r:
        m = (l+r) // 2
        val = m * m
        if val == x:
            return True
        elif val < x:
            l = m + 1
        else:
            r = m - 1
    return False

print(is_perfect_square(7))