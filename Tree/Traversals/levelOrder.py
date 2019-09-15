def levelOrder(root):
    q = [root]
    while q:
        node = q.pop(0)
        print(node, sep=' ', end=' ', flush=True)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
