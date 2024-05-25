def maxSubArray(nums):
        maxSum = float('-inf')
        curSum = 0

        for num in nums: 
            curSum += num 

            if curSum > maxSum:
                maxSum = curSum 

            if curSum < 0: 
                curSum = 0
        
        return maxSum