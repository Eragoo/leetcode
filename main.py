from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        m = prices[0]
        for i in range(1, len(prices)):
            el = prices[i]
            cm = el - m
            if max < cm:
                max = cm
            if el < m:
                m = el
        return max

if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))