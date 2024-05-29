# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(root, k):
        hash_map = dict()

        def dfs(root):
            if root is None:
                return

            if k - root.val in hash_map:
                return True
            
            hash_map[root.val] = True

            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)