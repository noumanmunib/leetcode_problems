def subarraySum(nums, k):
        res = 0
        curSum = 0
        prefixSum = {0 : 1}

        for n in nums:
            curSum += n
            # sum - k
            diff = curSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + (prefixSum.get(curSum, 0))
        
        return res