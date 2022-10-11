#Postorder traversal of Binary Tree

def Post_Order_traversal(root):
  stack = []
  result = []
  while stack or root:
    while root:
      stack.append(root)
      root = root.left
    temp = stack[-1].right
    if temp:
      root = temp
    else:
      temp = stack.pop()
      result.append(temp.val)
      while stack or temp == stack[-1].right:
        temp = stack.pop()
        result.append(temp.val)
   return result
