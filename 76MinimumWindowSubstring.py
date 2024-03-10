class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        th = {}
        for i in t:
            th[i] = th.get(i, 0) + 1

        sh = {}
        for i in s:
            sh[i] = sh.get(i, 0) + 1


        i = 0
        j = len(s) - 1

        cur = s
        while True:
            for i in th:
                if i in sh and sh[i] >= th[i]:



def test(s, t, expected):
    print(Solution().minWindow(s, t) == expected)


if __name__ == '__main__':
    test('A','AA', '')
    test('ADOBECODEBANC','ABC', 'BANC')