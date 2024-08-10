def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        
        for i in range(len(nums)):
            if i == k - 1:
                return nums[i]
        