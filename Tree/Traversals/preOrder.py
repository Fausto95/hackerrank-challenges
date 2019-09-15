def preOrder(root):
    #Write your code here
    if(root is None): return
    print(root, sep=' ', end=' ', flush=True)
    preOrder(root.left)
    preOrder(root.right)
