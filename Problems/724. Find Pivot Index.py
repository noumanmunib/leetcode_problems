def pivotIndex(nums):
        runningSum = sum(nums)
        sumLeft = 0

        for i in range(len(nums)):
            sumLeft += nums[i]

            if runningSum == sumLeft: 
                return i
            
            runningSum -= nums[i]

        return -1