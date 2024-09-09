class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        halfList = len(nums) / 2
        count = dict()

        for num in nums:
            count[num] = count.get(num, 0) + 1
                
            if count[num] > halfList: 
                return num