class TreeNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None


def checkTreeIsBST(root: TreeNode) -> bool:
    Stack = []
    prev = None
    while Stack or root:
        while root:
            Stack.append(root)
            root = root.left
        root = Stack.pop()
        if prev and root.data <= prev.data:
            return False
        prev = root
        root = root.right
    return True

if __name__ == "__main__":
    root = TreeNode(9)
    root.left = TreeNode(6)
    root.right = TreeNode(10)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(11)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(5)
    root.left.right.right = TreeNode(8)

    if checkTreeIsBST(root):
        print("Tree is binary search tree")
    else:
        print("Tree is not binary search tree")
