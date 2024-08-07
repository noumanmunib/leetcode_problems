from collections import Counter

def countStudents(students, sandwiches):
        res = len(students)
        count = Counter(students)

        # # How counter works with hashmap: 
        # count = {}
        # for s in students: 
        #     if s not in count: 
        #         count[s] = 0
        #     count[s] += 1

        for s in sandwiches: 
            if count[s] > 0: 
                res -= 1 # Number of Students Unable to Eat Lunch
                count[s] -= 1
            else: 
                return res
        
        return res