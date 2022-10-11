#PreOrder traversal of Binary Tree


def pre_order_traversal(root):
  stack = []
  result = []
  while stack or root:
    if root:
      result.append(root.val)
      stack.append(root)
      root = root.left
    else:
      root = stack.pop()
      root = root.right
  return result
