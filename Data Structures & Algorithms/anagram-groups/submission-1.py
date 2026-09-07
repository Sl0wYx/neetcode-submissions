class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for n in strs:
            key = ''.join(sorted(n))
            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(n)

        return list(hashmap.values())
