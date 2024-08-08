def maxFrequencyElements(nums) -> int:
        M = {}
        maxFreq = 0

        # Iterate through the list and populate the dictionary
        for num in nums:
            if num in M:
                M[num] += 1
            else:
                M[num] = 1
            maxFreq = max(maxFreq, M[num])

        res = 0
        # Iterate through the dictionary to find elements with frequency equal to maxFreq
        for key, value in M.items():
            if value == maxFreq:
                res += value

        return res