# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS 
        if root == None: 
            return 0
        
        left_root = self.maxDepth(root.left)
        right_root = self.maxDepth(root.right)

        return 1 + max(left_root, right_root)