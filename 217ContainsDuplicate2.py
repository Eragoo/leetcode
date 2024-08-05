from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = set()
        for num in nums:
            if num in c:
                return True
            c.add(num)
        return False


if __name__ == '__main__':
    print(Solution().containsDuplicate([1,2,3,1]) == True)
    print(Solution().containsDuplicate([1,2,3,4]) == False)
    print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True)