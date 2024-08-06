from typing import List


# try sort array if smth happened
# read fucking description
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i, k in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            while l < r:
                a1 = nums[i]
                a2 = nums[l]
                a3 = nums[r]
                if a1 + a2 + a3 == 0:
                    res.append([a1, a2, a3])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif a1 + a2 + a3 > 0:
                    r -= 1
                elif a1 + a2 + a3 < 0:
                    l += 1

        return res


if __name__ == '__main__':
    print(Solution().threeSum([-2, 1, 1, 1, 0, 0,3, -1, 1, 2]))
    print(Solution().threeSum([-2, 1, 0, 0, 1, 2]))
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
    print(Solution().threeSum([0, 0, 0, 0]) == [[0, 0, 0]])
