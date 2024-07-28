def maxDepth(self, s: str) -> int:
        maxDepth = 0
        curDepth = 0

        for char in s: 
            if char == "(":
                curDepth += 1
                maxDepth = max(maxDepth, curDepth)
            elif char == ")":
                curDepth -= 1
        
        return maxDepth