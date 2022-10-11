def printLeftView(root):
    if not root:
        return
    q = [root]  # [1]
    result = []
    while len(q):
        n = len(q)
        for i in range(1, n + 1):
            temp = q[0]
            q.pop(0)
            if i == 1:
                result.append(temp.data)
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
