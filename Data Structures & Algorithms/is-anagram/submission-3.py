class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        for c in s:
            seen[c] = seen.get(c, 0) + 1
        
        for c_t in t:
            if not seen.get(c_t):
                return False
            seen[c_t] -= 1
            if seen[c_t] == 0:
                del seen[c_t]

        return not seen