tokens = ["1","2","+","3","*","4","-"]
def evalRPN(tokens):
    stack = []
    char = "+*-/"
    for ch in tokens:
        if ch in char:
            a = stack.pop()
            b = stack.pop()
            if ch == "+":
                stack.append(a + b)
            elif ch == "-":
                stack.append(b - a)
            elif ch == "*":
                stack.append(a * b)
            else:
                stack.append(a/b)
        else:
            stack.append(int(ch))
    return stack[-1]

print(evalRPN(tokens))