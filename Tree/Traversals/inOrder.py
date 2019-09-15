def inOrder(root):
    #Write your code here
    if(root is None): return
    inOrder(root.left)
    print(root, sep=' ', end=' ', flush=True)
    inOrder(root.right)
