from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = res.get(num, 0) + 1

        res = {k: v for k, v in sorted(res.items(), key=lambda item: item[1], reverse=True)}
        r = [0] * k
        for i in range(0,k):
            r[i] = list(res.keys())[i]
        return r


if __name__ == '__main__':
    print(Solution().topKFrequent([1,1,1,2,2,3], 2))