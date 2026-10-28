class Solution:
    def isValid(self, s: str) -> bool:
        # using stack as our ds we will map closing bracket to opening bracket. we will pop every char 
        stack = []
        closeToOpen = {')':'(',']':'[','}':'{'}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: # stack[-1] last value added in the stack
                    stack.pop()
                else:
                    return False
            else: stack.append(c)
        
        return True if not stack else False
