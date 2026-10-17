class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i, n in enumerate(digits):
            digits[i] = str(n)

        str_numb = str(int("".join(digits)) + 1)
        
        res = []

        for c in str_numb:
            res.append(int(c))

        return res