from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (end + start) // 2
            mid_e = nums[mid]

            if mid_e == target:
                return mid

            # mid in left part
            if nums[start] <= mid_e:
                if target > mid_e or target < nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1
            # mid in right part
            else:
                if target < mid_e or target > nums[end]:
                    end = mid - 1
                elif target > mid_e:
                    start = mid + 1

        return -1

if __name__ == '__main__':
    print(Solution().search([4,5,6,7,0,1,2], 3))
    print(Solution().search([1,3,5], 1))
    print(Solution().search([5,1,3], 5))
