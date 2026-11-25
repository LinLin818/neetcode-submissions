class TimeMap:

    def __init__(self):
        self.store = {}  # key -> list of (timestamp, value), sorted by timestamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store.get(key, [])
        res = ""
        l, r = 0, len(pairs) - 1
        while l <= r:
            mid = (l + r) // 2
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]   # valid candidate; look right for a later one
                l = mid + 1
            else:
                r = mid - 1           # too late; look left
        return res
        
