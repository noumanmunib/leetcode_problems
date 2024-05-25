def kidsWithCandies(candies, extraCandies):
        max_candies = max(candies) 
        ans = []

        for i in range(len(candies)):
            ans.append(candies[i] + extraCandies >= max_candies)
        return ans

kidsWithCandies([1, 2, 6, 3, 3], 5)