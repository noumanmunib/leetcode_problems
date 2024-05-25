def getConcatenation(nums):
        ans = []
        for i in range(2):
            for n in nums: 
                ans.append(n)
        return ans

        # Time -> O(n + n) -> O(2n) -> O(n)
        # Space -> O(n) 