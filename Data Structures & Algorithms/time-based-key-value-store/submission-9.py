# hashmap timestore: key -> (value, timestamp)
# def set adds the value to the hashmap
# gets the valaue from the hashmap with binary search

class TimeMap:

    def __init__(self):
        self.timestore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestore[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestore or not self.timestore[key]:
            return ""

        entry = self.timestore[key]
        l, r = 0, len(entry) - 1

        while l <= r:
            m = (r + l) // 2

            if entry[m][1] == timestamp:
                return entry[m][0]
            elif entry[m][1] < timestamp:
                l = m + 1
            else:
                r = m - 1
        
        print(entry)
        return entry[r][0] if entry[r][1] <= timestamp else ""

