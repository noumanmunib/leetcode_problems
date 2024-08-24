# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):
            if not node: 
                return True
            
            left_height = height(node.left)
            right_height = height(node.right)

            if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1: 
                return -1 # Return -1 to indicate that the tree is unbalanced
            
            return max(left_height, right_height) + 1

        # Check the result of height; if it is -1, the tree is unbalanced
        return height(root) != -1            

# time -> O(n)
# space -> O(h) => O(n)