import math
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * (n)
        ans[0] = nums[0]
        for i in range(1, len(ans)):
            ans[i] = ans[i-1] * nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            pref = ans[i-1] if i-1 >= 0 else 1
            ans[i] = postfix * pref
            postfix *= nums[i]

        return ans


if __name__ == '__main__':
    print(Solution().productExceptSelf([1,2,3]))
