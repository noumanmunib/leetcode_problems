class Solution:
    def largestNumber(self, nums) -> str:
        
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            
            length = len(nums) // 2
            
            l = merge_sort(nums[:length])
            r = merge_sort(nums[length:])
            return merge(l, r)
        
        def merge(l, r):         
            res = []
            i, j = 0, 0

            while i < len(l) and j < len(r):
                if int(str(l[i]) + str(r[j])) > int(str(r[j]) + str(l[i])):
                    res.append(l[i])
                    i += 1
                else: 
                    res.append(r[j])
                    j += 1

            while i < len(l):
                res.append(l[i])
                i += 1
            while j < len(r):
                res.append(r[j])
                j += 1

            return res

        new_nums = merge_sort(nums)

        return str(int("".join(map(str, new_nums))))


        