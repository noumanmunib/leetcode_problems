class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): 
            return False
        
        subsequence = 0
        for i in range(len(t)):
            if subsequence == len(s):  # Check if subsequence index is out of bounds
                break
            if s[subsequence] == t[i]: 
                subsequence += 1 
    
        return subsequence == len(s)