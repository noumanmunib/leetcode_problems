def findLucky(arr):
        resArr = [-1]
        hashSet = set(arr)

        for value in hashSet: 
            if arr.count(value) == value: 
                resArr.append(value)
        
        return max(resArr)