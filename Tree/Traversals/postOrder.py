def postOrder(root):
    #Write your code here
    if(root is None): return
    postOrder(root.left)
    postOrder(root.right)
    print(root, sep=' ', end=' ', flush=True)
