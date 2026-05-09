# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def visit(self, root, depth):
        if not root:
            return 0
        
        return max(self.visit(root.left, depth + 1), self.visit(root.right, depth + 1), depth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.visit(root, 1)