from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        cur_max = 0
        while r < len(prices) and l <= r:
            cur_p = prices[r] - prices[l]
            if cur_p > cur_max:
                cur_max = cur_p
                r+=1
            elif cur_p < 0:
                l += 1
                r = l + 1
            else:
                r+=1
        return cur_max


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
