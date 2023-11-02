from collections import defaultdict
from typing import List


def topKFrequent1(nums: List[int], k: int) -> List[int]:
    dic = defaultdict(int)
    for n in nums:
        dic[n] += 1
    tuples = sorted(dic.items(), key=lambda x: x[1], reverse=True)[0:k]

    resp = []
    for i in tuples:
        resp.append(i[0])
    return resp


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for c, v in count.items():
        freq[v].append(c)

    resp = []
    for i in range(len(freq) - 1, 0, -1):
        for el in freq[i]:
            resp.append(el)
            if len(resp) == k:
                return resp



if __name__ == '__main__':
    print(topKFrequent([4,1,-1,2,-1,2,3], 2))
