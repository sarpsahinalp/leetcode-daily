class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        el = self.store.get(key)
        if el is not None:
            el.append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        # Get the list
        print(key, timestamp)
        print(self.store)
        values = self.store.get(key)

        if values is None:
            return ""

        # Find the first value that is closer to timestamp
        res = ""
        start = 0
        end = len(values) - 1

        while start <= end:
            mid = (start + end) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                start = mid + 1
            else:
                end = mid - 1

        return res
