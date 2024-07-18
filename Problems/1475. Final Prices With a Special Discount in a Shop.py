class Solution:
    def finalPrices(prices):
        answer = prices[:]
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                index = stack.pop()
                answer[index] -= prices[i]
            
            stack.append(i)

        return answer

        # Time -> O(n)
        # Space -> O(n)
