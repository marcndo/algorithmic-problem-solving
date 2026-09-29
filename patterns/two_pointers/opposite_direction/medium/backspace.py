def back_space_compare(s, t):
    s_stack = []
    t_stack = []
    for ch in s:
        if ch != "#":
            s_stack.append(ch)
        else:
            s_stack.pop()
    for ch in t:
        if ch != "#":
            t_stack.append(ch)
        else:
            t_stack.pop()
    if len(t_stack) != len(s_stack):
        return False
    for i in range(len(s_stack)):
        if s_stack[i] != t_stack[i]:
            return False
    return True

def optimal(s, t):
    i, j = len(s) - 1, len(t) - 1
    skip_s, skip_t = 0, 0

    while i >= 0 or j >= 0:
        while i >= 0:
            if s[i] == '#':
                skip_s += 1
                i -= 1
            elif skip_s > 0:
                skip_s -= 1
                i -= 1
            else:
                break

        while j >= 0:
            if t[j] == '#':
                skip_t += 1
                j -= 1
            elif skip_t > 0:
                skip_t -= 1
                j -= 1
            else:
                break

        if i >= 0 and j >= 0:
            if s[i] != t[j]:
                return False
        elif i >= 0 or j >= 0:
            return False

        i -= 1
        j -= 1

    return True
