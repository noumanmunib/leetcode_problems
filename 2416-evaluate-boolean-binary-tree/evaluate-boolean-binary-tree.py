# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0 or root.val == 1: 
            return bool(root.val)
        
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)

        if root.val == 2:
            return left_val or right_val
        if root.val == 3: 
            return left_val and right_val
        
        return root