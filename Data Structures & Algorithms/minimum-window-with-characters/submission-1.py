from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        t_freq = Counter(t)
        min_string = float("+inf")
        res = ""

        have = 0
        need = len(t_freq)
        l, r = 0, 0

        while r < len(s):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in t_freq and window[c] == t_freq[c]:
                have += 1

            while have == need:
                
                if r - l + 1 < min_string:
                    res = s[l:r+1]
                    min_string = r - l + 1

                window[s[l]] -= 1
                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    have -= 1

                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

            
            r += 1

        return res
            
            