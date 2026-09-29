class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash grouped_strings: sorted string -> list of string
        # for loop going through every string in the list
        # Every string will be sorted and used as key for hash
        # Add not sorted string to the hash
        # Second loop going through grouped_strings.items() appending them to the result list
        # Return result list
        # O(n * k log k)

        grouped_strings = {}

        # Grouping
        for string in strs:
            key = "".join(sorted(string))

            if key not in grouped_strings:
                grouped_strings[key] = []

            grouped_strings[key].append(string)

        # Returning the needed list
        result = []

        for key, group in grouped_strings.items():
            result.append(group)

        return result