from typing import List


# try sort array if smth happened
# read fucking description
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i, k in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
                elif sum3 > 0:
                    r -= 1
                elif sum3 < 0:
                    l += 1
        return res


if __name__ == '__main__':
    print(Solution().threeSum([-2, 1, 1, 1, 0, 0, 3, -1, 1, 2]))
    print(Solution().threeSum([-2, 1, 0, 0, 1, 2]))
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
    print(Solution().threeSum([0, 0, 0, 0]) == [[0, 0, 0]])
