class TimeMap:
    # 없을시에는 가장 큰 timemap의 value를 return, 아예 없다면 ""
    # 최초 key에 대한 value를 모아놓고
    # dic={'foo':[[1,'bar'],[4,'bar2]]}
    # 이진탐색으로 해야겠네
    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        values = self.time_map[key]
        start, end = 0, len(values) - 1
        result = ""
        while start <= end:
            mid = (start + end) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                start = mid + 1
            else:
                end = mid - 1
        return result