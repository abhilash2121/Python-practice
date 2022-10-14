from sys import maxsize as INT_MAX
from collections import namedtuple


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


Info = namedtuple('Info', ['max', 'min', 'isBST', 'sum', 'currmax'])
INT_MIN = -INT_MAX


def MaxSumBSTUtil(root: Node) -> Info:
    global maxsum

    if root is None:
        return Info(INT_MIN, INT_MAX,
                    True, 0, 0)

    if (root.left is None and
            root.right is None):
        maxsum = max(maxsum,
                     root.data)
        return Info(root.data, root.data,
                    True, root.data, maxsum)

    L = MaxSumBSTUtil(root.left)
    R = MaxSumBSTUtil(root.right)

    BST = Info

    if (L.isBST and R.isBST and
            L.max < root.data < R.min):
        BST.max = max(root.data,
                      max(L.max, R.max))
        BST.min = min(root.data,
                      min(L.min, R.min))

        maxsum = max(maxsum, R.sum +
                     root.data + L.sum)
        BST.sum = R.sum + root.data + L.sum

        # Update the current maximum sum
        BST.currmax = maxsum

        BST.isBST = True
        return BST

    # If the whole tree is not
    # a BST then update the
    # current maximum sum
    BST.isBST = False
    BST.currmax = maxsum
    BST.sum = R.sum + root.data + L.sum
    return BST


def MaxSumBST(root: Node) -> int:
    global maxsum
    return MaxSumBSTUtil(root).currmax


# Driver code
if __name__ == "__main__":
    root = Node(5)
    root.left = Node(14)
    root.right = Node(3)
    root.left.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(9)
    root.left.left.right = Node(1)

    maxsum = INT_MIN
    print(MaxSumBST(root))
