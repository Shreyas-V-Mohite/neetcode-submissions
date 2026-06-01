class Solution:
    def isValid(self, s: str) -> bool:
    # TRICK: Stack (LIFO). Push opening brackets. When hitting a closing bracket,
    # it MUST match the top of the stack (the most recent open bracket).
    # A mismatch or an empty stack means invalid; must end with an empty stack.
        stack = []
        closeToOpen = {"}":"{",")":"(","]":"["}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
