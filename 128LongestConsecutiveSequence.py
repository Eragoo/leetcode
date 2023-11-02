from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        elems = set(nums)

        gt = 1
        for el in elems:
            curr_gt = 1
            if (el - 1) not in elems:
                i = 1
                while (el + i) in elems:
                    curr_gt += 1
                    i += 1
            gt = max(curr_gt, gt)

        return gt


if __name__ == '__main__':
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
