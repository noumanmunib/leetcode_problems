class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res=[]
        q = collections.deque()
        q.append(root)
        while(q):
            level=[]
            qlen =len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(sum(level)/len(level))

        return res