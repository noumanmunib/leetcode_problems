class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, pathVal):
            if not node: 
                return 0

            pathVal = (pathVal << 1) + node.val

            if not node.left and not node.right: # if reached leaf node
                return pathVal

            return dfs(node.left, pathVal) + dfs(node.right, pathVal)
        
        return dfs(root, 0)
            

# path=0 => (path<<1) + 1 = 01
# path=01 => (path<<1) + 1 = 11
# path=11 => (path<<1) + 0 = 110
# path=110 => (path<<1) + 1 = 1101