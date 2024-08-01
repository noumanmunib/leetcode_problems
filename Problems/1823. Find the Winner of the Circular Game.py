class Solution:
    def findTheWinner(n, k):
        winner = 0
        for i in range(1, n+1):
            winner = (k + winner) % i
            print(winner + 1) # This will print the winner in the i-person case

        return winner + 1

# Time -> O(n)
# Space -> O(1)