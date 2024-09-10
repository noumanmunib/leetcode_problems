class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1Idx = {}
        # for i in range(len(nums1)):
        #     num = nums1[i]
        #     nums1Idx[num] = i

    # O(n . m) Solution: 
        nums1_Index = { num: i for i, num in enumerate(nums1) }
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1_Index: 
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    index = nums1_Index[nums2[i]]
                    res[index] = nums2[j]
                    break
        return res