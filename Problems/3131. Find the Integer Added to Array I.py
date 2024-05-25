def addedInteger(nums1, nums2):
    # x = min(nums2) - min(nums1)
    # return x

    nums1.sort()
    nums2.sort()
    
    return nums2[0] - nums1[0]
        

addedInteger([2,6,4], [9,7,5])