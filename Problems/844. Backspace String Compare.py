def backspaceCompare(s: str, t: str) -> bool:
        def processStr(string):
            stack = []

            for char in string: 
                if char != '#':
                    stack.append(char)
                elif stack: 
                    stack.pop()

            return stack

        return processStr(s) == processStr(t)