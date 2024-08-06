from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = dict()
        for i in range(0, len(nums)):
            n = nums[i]
            if n in diff.keys():
                return [diff[n], i]
            diff[target - n] = i
        return []

if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15], 9))