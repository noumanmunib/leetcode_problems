class Solution:
    def minDiffInBST(self, root) -> int:
        res = []

        def inorder(root): 
            if not root: 
                return

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            return
            
        ans = 100000
        inorder(root)
        for i in range(1, len(res)): 
            value = res[i] - res[i-1]
            ans = min(ans, value)

        return ans