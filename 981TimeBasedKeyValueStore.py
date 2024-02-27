class TimeMap:
    store = {}

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            values = self.store[key]
        else:
            values = []
        values.append([timestamp, value])
        self.store[key] = values

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            arr = self.store[key]
        else:
            return ""

        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (l + r) // 2

            curr = arr[mid][0]

            if curr == timestamp:
                return arr[mid][1]

            if curr < timestamp:
                l = mid + 1
            elif curr > timestamp:
                r = mid - 1
        if arr[r][0] > timestamp:
            return ""
        return arr[r][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

if __name__ == '__main__':
    operations = ["TimeMap","set","set","get","set","get","get"]
    # operations = ["TimeMap","set","set","get","get","get","get","get"]
    # operations = ["TimeMap","set","get","get","set","get","get"]
    # values = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
    values = [[],["a","bar",1],["x","b",3],["b",3],["foo","bar2",4],["foo",4],["foo",5]]
    # values = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

    tm = TimeMap()
    for i in range(1, len(operations)):
        op = operations[i]
        val = values[i]

        if op=="set":
            tm.set(val[0], val[1], val[2])
        if op=="get":
            el = tm.get(val[0], val[1])
            print("Element: " + el + " Val: " + val[0] + ":" + str(val[1]))

