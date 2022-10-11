#Lowest common ancestor of two nodes in Binary tree

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root.val == p or root.val == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if right and left:
            return root
        return right or left
