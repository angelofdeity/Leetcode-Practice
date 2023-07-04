class Solution:
    """
    Possibe solution 1
    Use a stack to keep track of the opening brackets.
    If the closing bracket matches the top of the stack, pop the stack.
    If the stack is empty, return True.
    """

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '[{(':
                stack.append(c)
            elif not stack:
                return False
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            elif c == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False
        return True if not stack else False


class Solution:
    """
    Possible solution 2
    Use a stack to keep track of the opening brackets.
    Use a dictionary to map the opening brackets to the closing brackets.
    If the closing bracket matches the top of the stack, pop the stack.
    If the stack is empty, return True.
    """

    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for c in s:
            if c in pair:
                stack.append(c)
            elif not stack or c != pair[stack.pop()]:
                return False
        return not stack
