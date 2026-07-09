class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        for s in strs:
            key = ''.join(sorted(s))
            grouped[key] = grouped.get(key, [])

            grouped[key].append(s)

        ans = [x for x in grouped.values()]
        return ans