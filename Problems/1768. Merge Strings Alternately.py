def mergeAlternately(word1, word2):
        i = 0
        ans = ""

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                ans = ans + word1[i]

            if i < len(word2):
                ans = ans + word2[i]

            i = i + 1
        
        return ans 