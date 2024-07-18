def removeOuterParentheses(s):
        res, opened = [], 0

        for char in s:
            if char == "(" and opened > 0:
                res.append(char)
            if char == ")" and opened > 1:
                res.append(char)
            
            opened += 1 if char == "(" else -1
        
        return "".join(res)
