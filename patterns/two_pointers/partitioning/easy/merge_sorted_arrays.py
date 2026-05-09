def merge(num1, m, num2, n):
    p1 = m - 1
    p2 = n - 1
    j = m + n - 1
    while p2 >= 0:
        if p1 >= 0 and num1[p1] > num2[p2]:
            num1[j] = num1[p1]
            p1 -= 1
        else:
            num1[j] = num2[p2]
            p2 -= 1
        j -= 1
    return num1