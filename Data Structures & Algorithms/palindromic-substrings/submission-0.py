class Solution:
    def countSubstrings(self, s: str) -> int:
        s_len = len(s)
        dp = [[False] * s_len for _ in range(s_len)]
        count = 0

        for length in range(1, s_len + 1):
            for i in range(s_len - length + 1):
                j = i + length - 1

                if s[i] == s[j] and (length <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1
        
        return count
