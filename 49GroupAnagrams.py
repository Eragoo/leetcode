from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord("a")] += 1
            dict[tuple(count)].append(str)

        return dict.values()






if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))