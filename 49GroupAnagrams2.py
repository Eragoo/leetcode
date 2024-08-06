from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            p = [0] * 26
            for c in s:
                p[ord(c) - ord("a")] += 1
            res[tuple(p)].append(s)

        return res.values()

if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))