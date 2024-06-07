def findMaxConsecutiveOnes(nums):
        count = 0
        maxi = 0

        for n in nums: 
            if n == 1: 
                count += 1
            else: 
                count = 0
            
            if count > maxi: 
                maxi = count
        
        return maxi