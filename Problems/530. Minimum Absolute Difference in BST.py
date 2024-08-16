class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        # Helper function to perform in-order traversal of the binary tree.
        # This will collect the values of the nodes in a sorted order (for a BST).
        def inorderTraversal(root):
            res = []

            if root:
                # Recursively visit the left subtree
                res = inorderTraversal(root.left)
                # Append the current node's value
                res.append(root.val)
                # Recursively visit the right subtree
                res = res + inorderTraversal(root.right)
            return res

        # Helper function to find the minimum difference between consecutive elements in a sorted list
        def findMinDiff(arr, n):
            diff = 10**20  # Initialize with a very large number

            # Iterate through the sorted array and find the smallest difference
            for i in range(n - 1):
                if arr[i + 1] - arr[i] < diff:
                    diff = arr[i + 1] - arr[i]

            return diff

        # Perform in-order traversal of the binary tree and store the result in a list
        res = inorderTraversal(root)
        n = len(res)  # Get the length of the result list

        # Find the minimum difference between consecutive values in the sorted list
        ans = findMinDiff(res, n)

        return ans  # Return the minimum difference found
