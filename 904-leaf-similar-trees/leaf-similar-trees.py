# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:        
        s1 = self.getSequence(root1)
        s2 = self.getSequence(root2)

        if len(s1) != len(s2):
            return False
        return all(a == b for a, b in zip(s1, s2))

    def getSequence(self, root):
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, root, result):
        if root is None: 
            return 
        
        if not root.left and not root.right: 
            result.append(root.val)
            return
        
        self.dfs(root.left, result)
        self.dfs(root.right, result)
                


        
        
