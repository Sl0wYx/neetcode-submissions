class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l, r = 0, 0
        max_length = 0

        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1

            while r - l + 1 - max(window.values()) > k:   
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

            if len(window) > 1 and min(window.values()) <= k:
                max_length = max(max_length, r - l + 1) 
            else:
                max_length = max(max_length, r - l + 1) 
                
            r += 1

        return max_length