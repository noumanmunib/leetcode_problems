class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: 
            return 0
        
        low = 1
        high = x

        while low <= high: 
            mid = low + (high - low) // 2 # This formula avoids potential overflow

            if mid == x // mid:
                return mid
            elif mid > x // mid: 
                high = mid - 1
            else: 
                low = mid + 1
        
        return high

        