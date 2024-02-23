from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = nums[0]
        e_i = len(nums) - 1
        e = nums[e_i]

        if s < e or s == e:
            return nums[0]

        start = 0
        end = e_i

        def inx(i, n):
            if i > n:
                return i % n - 1
            if i < 0:
                return n + i
            return i

        while start < end:
            mid = int(start + ((end - start) / 2))
            mid_e = nums[mid]

            mid_l = nums[inx(mid - 1, e_i)]
            mid_r = nums[inx(mid + 1, e_i)]

            if mid_e < mid_l or mid_e > mid_r:
                return min(mid_e, mid_l, mid_r)

            if mid_e < e and mid_e < s:
                end = mid - 1
            if mid_e > s and mid_e > e:
                start = mid + 1

        return -1


if __name__ == '__main__':
    # print(Solution().findMin([2,3,4,5,1]))
    print(Solution().search([2], 2))

