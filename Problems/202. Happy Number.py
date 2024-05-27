def isHappy(n):
    hashSet = set()

    while True: 
        cSum = 0
        while n > 0: 
            n_dash = n % 10
            cSum += (n_dash * n_dash)
            n = n // 10

        if cSum == 1:
            return True
        elif cSum in hashSet:
            return False
        else:
            hashSet.add(cSum)
            n = cSum
    return None
        
isHappy(19)