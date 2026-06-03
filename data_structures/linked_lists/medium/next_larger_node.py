def nextLargerNodes(head):
    # step 1 — convert to array
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next

    # step 2 — monotonic stack
    answer = [0] * len(vals)
    stack  = []             
    for i, val in enumerate(vals):
        while stack and vals[stack[-1]] < val:
            idx = stack.pop()
            answer[idx] = val 
        stack.append(i)

    return answer