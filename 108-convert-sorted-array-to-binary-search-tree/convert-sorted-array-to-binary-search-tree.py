# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: 
            return

        # Since it is BST: 
        mid = len(nums) // 2

        # create the root of the tree with nums[mid]:
        root = TreeNode(nums[mid])

        # recursively add the nums values to the left and right subtrees of the root:
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        # return the root tree.
        return root
        