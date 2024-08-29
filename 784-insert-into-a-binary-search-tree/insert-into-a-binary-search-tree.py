# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Iterative solution: 
        if not root: 
            return TreeNode(val)

        cur = root
        while True: 
            if val > cur.val:
                if not cur.right: 
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
            
            if val < cur.val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left 
            

    # worst time -> O(h)
    # space -> O(1)