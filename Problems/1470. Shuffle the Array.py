def shuffle(nums, n):    
        new = []

        for i in range(0, n):
            new.append(nums[i])
            new.append(nums[i + n])
        
        return new