def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right: 
        mid = (left + right ) // 2

        if nums[mid] < nums[right]:
            right = mid

        else: 
            left = mid + 1
    
    return nums[left]

numsList = findMin([1, 2, 3])

print(numsList)