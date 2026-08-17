class TimeMap:

    def __init__(self):
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key] = self.values.get(key, [])
        self.values[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if self.values.get(key) is None:
            return ""
        key_list = self.values[key]
        l, r = 0, len(key_list) - 1

        while l <= r:
            m = (r + l) // 2

            if key_list[m][1] == timestamp:
                return key_list[m][0]
            elif key_list[m][1] > timestamp:
                r = m - 1
            else:
                l = m + 1

        return key_list[r][0] if key_list[r][1] < timestamp else ""
