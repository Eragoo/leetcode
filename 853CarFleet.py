from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([[p, s] for p, s in zip(position, speed)])
        cars.reverse()

        res = 0
        max_time = -1
        for p, s in cars:
            cur_time = (target - p) / s
            if max_time != -1 and max_time >= cur_time:
                res -= 1
            if cur_time > max_time:
                max_time = cur_time
            res += 1

        return res


if __name__ == '__main__':
    print(Solution().carFleet(10, [0, 4, 2], [2, 1, 3]))
