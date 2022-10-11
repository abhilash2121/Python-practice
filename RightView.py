def printRightView(root):
    if not root:
        return
    q = [root]  # [2,6,7]
    result = []
    while len(q):
        n = len(q)
        for i in range(1, n + 1):
            temp = q[-1]
            q.pop(-1)
            if i == 1:
                result.append(temp.val)
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
    return result
