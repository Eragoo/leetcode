import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(piles, speed) -> int:
            cur_h = 0
            for pile in piles:
                cur_h += math.ceil(pile / speed)
            return cur_h

        s = 1
        e = max(piles)

        piv = int(s + (e - s) / 2)
        while s < e:
            piv = int(s + (e - s) / 2)
            c = eat(piles, piv)
            if c > h:
                s = piv + 1
            elif c <= h:
                e = piv

        last = eat(piles, int(s + (e - s) / 2))
        if last <= h:
            return int(s + (e - s) / 2)
        return piv




if __name__ == '__main__':
    print(Solution().minEatingSpeed([312884470], 312884469) == 2)
    print(Solution().minEatingSpeed([3,6,7,11], 8) == 4)
    print(Solution().minEatingSpeed([30,11,23,4,20], 5) == 30)
    print(Solution().minEatingSpeed([30,11,23,4,20], 6) == 23)
    print(Solution().minEatingSpeed([332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184], 823855818) == 14)

