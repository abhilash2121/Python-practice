def zizagtraversal(root):
    if root is None:
        return

    currentLevel = []
    nextLevel = []
    result = []

    ltr = True

    currentLevel.append(root)

    while len(currentLevel) > 0:
        temp = currentLevel.pop(-1)
        result.append(temp.data)

        if ltr:
            if temp.left:
                nextLevel.append(temp.left)
            if temp.right:
                nextLevel.append(temp.right)
        else:
            if temp.right:
                nextLevel.append(temp.right)
            if temp.left:
                nextLevel.append(temp.left)

        if len(currentLevel) == 0:
            ltr = not ltr
            currentLevel, nextLevel = nextLevel, currentLevel
    return result
