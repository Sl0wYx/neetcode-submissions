class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash grouped: sorted string keys -> strings
        # for loop to go through each string in strs
        # Sort current string and add it as key with empty list to the hash
        # Add current string to the hash keyed with the same string but sorted
        # Return list of .values of grouped hash
        # Time: O(n * k log k) Space: O(n)
    
        grouped = {}

        for string in strs:
            key = "".join(sorted(string))
            
            if key not in grouped:
                grouped[key] = []
                
            grouped[key].append(string)
        
        return list(grouped.values())


