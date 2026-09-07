class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        current_max = 0

        current_subs = set()
        l = 0

        for r in range(len(s)):
            while s[r] in current_subs:
                current_subs.remove(s[l])
                l += 1

            current_subs.add(s[r])
            max_length = max(r - l + 1, max_length)

        return max_length
            