def sortColors(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # l, r = 0, len(nums) - 1

        # i = 0

        # def swap(i, j):
        #     temp = nums[i]
        #     nums[i] = nums[j]
        #     nums[j] = temp

        # while i <= r: 
        #     if nums[i] == 0: 
        #         swap(l, i)
        #         l += 1
        #     elif nums[i] == 2:
        #         swap(i, r)
        #         r -= 1
        #         i -= 1
        #     i += 1

        zeroes, ones, n = 0, 0, len(nums)

        for num in nums: 
            if num == 0:
                zeroes += 1
            elif num == 1: 
                ones += 1
        
        for i in range(0, zeroes):
            nums[i] = 0
            
        for i in range(zeroes, zeroes + ones):
            nums[i] = 1
        
        for i in range(zeroes + ones, n):
            nums[i] = 2