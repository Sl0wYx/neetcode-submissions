class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()

        l = 0
        max_length = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1

            max_length = max(max_length, r - l + 1)
            window.add(s[r])

        return max_length
