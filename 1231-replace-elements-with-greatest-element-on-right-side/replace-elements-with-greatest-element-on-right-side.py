class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        # reverse iteration
        # new max = max(old max, arr[i])

        maxRight = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(maxRight, arr[i])
            arr[i] = maxRight
            maxRight = newMax

        return arr
    
    # time -> O(n)
    # space -> O(1)