from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nulls = {}
        for i in range(0, len(nums)):
            num = nums[i]
            if num == 0:
                nulls[i] = True

        aen = 1
        for i in range(0, len(nums)):
            if i not in nulls.keys():
                aen *= nums[i]


        res = []
        if len(nulls) == 0:
            for num in nums:
                res.append(int(aen / num))
            return res

        res = [0] * len(nums)
        if len(nulls) == 1:
            for k, v in nulls.items():
                res[k] = aen

        return res


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))
    print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
    print(Solution().productExceptSelf([0, 1, 0, -3, 3]))
