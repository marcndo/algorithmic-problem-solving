def postorder(root):
    result = []
    def bfs(node):
        if not node:
            return 
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    dfs(root)
    return result