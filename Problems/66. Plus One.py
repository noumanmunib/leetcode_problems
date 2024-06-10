def plusOne(digits):
        n = len(digits) - 1
        
        while digits[n] == 9: 
            digits[n] = 0
            n -= 1

        if n < 0: 
            return [1] + digits

        digits[n] += 1

        return digits