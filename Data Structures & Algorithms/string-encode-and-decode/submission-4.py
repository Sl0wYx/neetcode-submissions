from collections import Counter
class Solution:
    def encode(self, strs: List[str]) -> str:
        e_list = ""
        for i in range(len(strs)):
            e_list += strs[i] + ":;"

        return e_list
    def decode(self, s: str) -> List[str]:
        decoded = s.split(':;')[:-1]

        return decoded
                