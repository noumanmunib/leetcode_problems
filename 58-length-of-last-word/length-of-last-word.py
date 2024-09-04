class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Initialize the pointer denoting end of the last word from the end of the string
        end = len(s) - 1

        # Decrement the end pointer if the last char is a space
        while s[end] == " ": 
            end -= 1

        # initialize the pointer denoting start of the last word to be found
        start = end
        # decrement start pointer as long is it doesn t reaches the next space in string
        while start >= 0 and s[start] != " ":
            start -= 1

        # return the length between start and end pointers 
        return end - start
        
