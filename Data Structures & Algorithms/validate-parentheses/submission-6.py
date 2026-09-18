class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {")":"(", "}":"{", "]":"["}
        stack = []

        for c in s:
            if c in par_map:
                if not stack:
                    return False
                if stack[-1] != par_map[c]:
                    return False
                stack.pop()
            else: stack.append(c)


        return not stack
            