def match_characters(exp):
    left = "({["
    right = ")}]"
    stack = []
    for ch in exp:
        if ch in left:
            stack.append(ch)
        elif ch in right:
            if len(stack) == 0:
                return False
            elif right.index(ch) != left.index(stack.pop()):
                return False
    return len(stack) == 0