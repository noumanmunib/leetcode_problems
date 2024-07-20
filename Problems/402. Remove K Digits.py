def removeKdigits(num, k):
        stack = []

        for char in num:
            while stack and stack[-1] > char and k > 0:
                stack.pop()  
                k -= 1
            stack.append(char)

        stack = stack[:len(stack) - k]

        res="".join(stack)

        return str(int(res)) if res else "0" or "0"

removeKdigits("1432219", 3)