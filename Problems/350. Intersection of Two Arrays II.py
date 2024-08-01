def intersect(nums1, nums2):
        nums1.sort()
        nums2.sort()

        i = j = 0
        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else: 
                res.append(nums2[j])
                i += 1
                j += 1
        
        return res

# Time -> O(nlog n + mlog m)
# Space -> O(min(n, m))