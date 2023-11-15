from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i_l = 0
        i_r = len(height) - 1
        max = 0
        while i_l <= i_r:
            r_ = height[i_r]
            l_ = height[i_l]
            cur_max = (i_r - i_l) * min(r_, l_)
            if cur_max > max:
                max = cur_max

            if r_ < l_:
                i_r += -1
            else:
                i_l += 1
        return max

if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
