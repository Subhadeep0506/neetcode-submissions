class TimeMap:
    def __init__(self):
        self.time_map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map.get(key, [])
        start, end = 0, len(values) - 1
        res = ""
        while start <= end:
            mid = (start + end) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                start = mid + 1
            else:
                end = mid - 1
        return res
