def isSameTree(p, q):
    if not p and not q:
        return True
    
    queue = deque()
    queue.append((p, q))
    
    while queue:
        left, right = queue.popleft()
        
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        
        queue.append((left.left, right.left))
        queue.append((left.right, right.right))
    
    return True