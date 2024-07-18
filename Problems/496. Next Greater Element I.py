def nextGreaterElement(nums1, nums2):
        # nums1Idx = {}
        # for i in range(len(nums1)):
        #     num = nums1[i]
        #     nums1Idx[num] = i

        nums1Idx = {num: i for i, num in enumerate(nums1) }
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop() 
                index = nums1Idx[val]
                res[index] = cur
            
            if cur in nums1Idx: 
                stack.append(cur)
        return res

    # Time => O(n + m)
    # Space => O(n)