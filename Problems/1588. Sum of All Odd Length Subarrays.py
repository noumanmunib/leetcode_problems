def sumOddLengthSubarrays(arr):
        n=len(arr)
        s=0

        for i in range(n):
            s+=((i+1)*(n-i)+1)//2*arr[i]
            
        return s