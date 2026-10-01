class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashmap window:character -> index ma
        # for loop with window validation
        # track max lenght
        # return max length

        window = {}
        max_length = 0

        l = 0
        for r, c in enumerate(s):
            while c in window:
                del window[s[l]]
                l += 1

            max_length = max(max_length, r - l + 1)
            window[c] = r

        return max_length

            