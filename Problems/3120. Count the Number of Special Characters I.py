def numberOfSpecialChars(word):
        res_set = set(word)
        count = 0

        for i in res_set:
            if i.lower() == i and i.upper() in res_set: 
                count += 1
        
        return count