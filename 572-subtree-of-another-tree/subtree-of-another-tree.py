# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if no subRoot, then it means any subtree can match, hence return true.
        if not subRoot:
            return True
        # if no root, then no nodes in the root tree, hence return False.
        if not root: 
            return False

        if self.same(root, subRoot):
            return True

        # recursively check if subRoot is a subtree of the left or right subtrees of the root.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # Helper function to check if two subtrees are identical
    def same(self, node, subNode):
        if not node and not subNode: 
            return True

        if node and subNode and node.val == subNode.val:
            #recursively check if the left and right subtrees of root and subRoot are identical.  
            return self.same(node.left, subNode.left) and self.same(node.right, subNode.right)

        # else the trees are not identical.
        return False

    # time -> O(n.m)
    # space -> O(h)
        