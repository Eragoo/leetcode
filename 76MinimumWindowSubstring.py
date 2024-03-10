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



        def check(th, sh):
            for i in th:
                if i not in sh or sh[i] < th[i]:
                    return False
            return True

        if not check(th, sh):
            return ""

        def decrease(sh, idx):
            if sh[s[idx]] <= 1:
                sh.pop(s[idx])
            else:
                sh[s[idx]] = sh[s[idx]] - 1

        i = 0
        j = len(s) - 1
        moved_i = True
        moved_j = True
        while True:
            if not moved_i and moved_j:
                break

            decrease(sh, i)
            if check(th, sh):
                i += 1
                moved_i = True
            else:
                sh[i] = sh.get(i, 0) + 1
                moved_i = False


            decrease(sh, j)
            if check(th, sh):
                j -= 1
                moved_j = True
            else:
                sh[j] = sh.get(j, 0) + 1
                moved_j = False

        return s[i:j]

def test(s, t, expected):
    print(Solution().minWindow(s, t) == expected)


if __name__ == '__main__':
    # test('A','AA', '')
    # test('ABCD','AA', '')
    test('ADOBECODEBANC','ABC', 'BANC')