# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.max_diameter = 0
        def max_depth(root):
            if root == None:
                return 0
            
            left = max_depth(root.left)
            right = max_depth(root.right)

            if (left + right) > self.max_diameter:
                self.max_diameter = (left + right)

            return 1 + max(left, right)
        max_depth(root)
        return self.max_diameter

        