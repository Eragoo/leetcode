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
            if start <= mid_e:
                if target > mid_e:
                    start = mid + 1
                else:
                    if target == nums[end]:
                        return end
                    if target < nums[end]:
                        start = mid + 1
                        end = end - 1
                    if target > nums[end]:
                        start = 0
                        end = mid_e - 1

                # mid in right part
            else:
                if target > mid_e:
                    if target == nums[start]:
                        return start
                    if target > nums[start]:
                        start = start + 1
                        end = mid - 1
                    else:
                        start = mid + 1
                        end = end
                else:
                    end = mid - 1

        return -1

if __name__ == '__main__':
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
    # print(Solution().search([2], 2))
