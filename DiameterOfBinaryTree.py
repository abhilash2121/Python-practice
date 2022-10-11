#Diameter of Binary Tree

class Solution(object):
    def diameterOfBinaryTree(self, root):
        def height(node):
            if node == None:
                return 0
            left = height(node.left) # 0
            right = height(node.right) # 0
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1

        self.diameter = 0
        height(root)
        return self.diameter
