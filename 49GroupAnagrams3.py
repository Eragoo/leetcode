from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for str in strs:
            c = [0] * 26
            for e in str:
                c[ord(e) - ord("a")] += 1
            res[tuple(c)].append(str)
        return res.values()

if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))