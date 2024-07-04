class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brac_dict = {')': '(', ']': '[', '}' : '{'}

        for c in s:
            if c not in brac_dict:
                stack.append(c)
            else:
                if not stack or stack[-1] != brac_dict[c]: 
                    return False
                stack.pop()

        return not stack