# Level Order Travsersal of Binary Tree

def levelOrder(root):
    if not root:
        return None

    queue = [root]
    result = []
    while queue:
        arr = []
        for i in range(len(queue)):
            node = queue.pop(0)
            arr.append(node.val)
            left = node.left
            right = node.right
            if left:
                queue.append(left)
            if right:
                queue.append(right)
        result.append(arr)
    return result
