#Inorder traversal of Binary Tree


def in_order_traversal(root):
  stack = []
  result = []
  while stack or root:
    if root:
      stack.append(root)
      root = root.left
    else:
      root = stack.pop()
      result.append(root.val)
      root = root.right
  return result
