def min_depth(root):
    if not root:
        return 0
    left = min_depth(root.left)
    right = min_depth(root.right)
    if not root.left:
        return 1 + right
    if not root.right:
        return 1 + left
    return 1 + min(left, right)
