from collections import deque

class Solution:
    def firstUniqChar(s):
        # Create a queue to store the indices of characters
        queue = deque()
        # Create a dictionary to count the frequency of each character
        char_count = {}

        # Iterate over the string and update the queue and dictionary
        for i, char in enumerate(s):
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
                queue.append((char, i))
        
        # Process the queue to find the first unique character
        while queue:
            char, idx = queue.popleft()
            if char_count[char] == 1:
                return idx
        
        # If no unique character is found, return -1
        return -1