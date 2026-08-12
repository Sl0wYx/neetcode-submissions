from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        window = {}

        l, r = 0, 0

        while r < len(s2):
            window[s2[r]] = window.get(s2[r], 0) + 1
            while len(s1) < r - l + 1:
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]

                l += 1
            
            if s1_freq == window:
                return True

            r += 1
        
        return False