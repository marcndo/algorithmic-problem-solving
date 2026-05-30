def first_bad_version(n: int) -> int:
    l, r = 0, n
    while l + 1 < r:
        m = (l+r) // 2
        ver_status = isBadVersion(m)
        if vers_status == True:
            r = mid
        else:
            l = mide
        if isBadVersion(l):
            return l
    return r


