class Solution:
    def validParentheses(self, s:str):
        stack = []
        openToClose = {")" : "(", "}" : "{", "]" : "["}
        for c in s:
            if c in openToClose:
                if stack and stack[-1] == openToClose[c]:
                    stack.pop(c)
                else:
                    return False
            else: 
                stack.append(c)
        return True if not stack else False
