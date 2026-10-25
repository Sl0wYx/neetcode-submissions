class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        
        res = 0
        for word in words:
            word_count = Counter(word)
            if word_count <= chars_count:
                res += len(word)

        return res