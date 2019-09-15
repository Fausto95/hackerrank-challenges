def height(root):
    count = 0
    if root.left:
        count = 1 + height(root.left)
    if root.right:
        count = 1 + height(root.right)
    return count
