def maxOperations(nums, k):
        nums.sort()
        left, right = 0, len(nums) - 1
        res = 0

        while left < right: 
            sum_ = nums[left] + nums[right]

            if sum_ < k:
                left += 1
            elif sum_ > k:
                right -= 1
            else:
                res += 1
                left += 1
                right -= 1
        
        return res
