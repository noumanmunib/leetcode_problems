def groupAnagrams(strs):
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs: 
            count = [0] * 26 # a .... z
            
            for c in s: 
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)

        return res.values()

        # time complexity -> O(m . n)
        # space -> O(n)