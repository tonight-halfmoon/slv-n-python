class _NodeBinaryTree:
    def  __init__(self(), data):
        self.data = data
        self.left = None
        self.right = None
        
    def preorderTraversal (tree):
        if tree is not None:
            print(tree.data)
            preorderTraversal(tree.left) 
            preorderTraversal(tree.right)
    def inorderTraversal (tree):
        if tree is not None:
            inorderTraversal(tree.left)
            print(tree.data)
            inorderTraversal(tree.right)
    def postorderTraversal (tree):
        if tree is not None:
            postorderTraversal(tree.left)
            postorderTraversal(tree.right)
            print(tree.data)

    def bfs(tree):
        Queue q
        q.enqueue(tree)
        while not q.isEmpty(): 
            node = q.dequeue()
            print(node)
            if node.left is not None:
                q.enque(node.left)
            if node.right is not None:
                q.enque(node.right)
