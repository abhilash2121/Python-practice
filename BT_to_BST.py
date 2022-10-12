class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def InorderTraversal(root, result):
    if root is None:
        return
    InorderTraversal(root.left, result)
    result.append(root.data)
    InorderTraversal(root.right, result)


def countNodes(root):
    if root is None:
        return 0
    return countNodes(root.left) + countNodes(root.right) + 1


def arrayToBST(arr, root):
    if root is None:
        return
    arrayToBST(arr, root.left)
    root.data = arr[0]
    arr.pop(0)
    arrayToBST(arr, root.right)


def binaryTreeToBST(root):
    if root is None:
        return
    n = countNodes(root)
    arr = []
    InorderTraversal(root, arr)
    arr.sort()
    arrayToBST(arr, root)


root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right = Node(5)

binaryTreeToBST(root)
