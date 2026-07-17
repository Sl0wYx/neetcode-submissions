class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {']':'[', '}':'{', ')':'('}
        stack = []

        for c in s:
            if c in brackets:
                if not stack:
                    return False

                if brackets[c] != stack.pop():
                    return False
                else:
                    continue
            
            stack.append(c)
        
        return not stack