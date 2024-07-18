def calPoints(operations):
        scores = []

        if len(operations) == 0: 
            return

        for i, cur in enumerate(operations): 
            if cur == "C":
                scores.pop()
            elif cur == "D" and i != 0:
                scores.append(scores[-1] * 2)
            elif cur == "+" and i != 0: 
                scores.append(scores[-1] + scores[-2])
            else: 
                scores.append(int(cur))
        
        return sum(scores)
