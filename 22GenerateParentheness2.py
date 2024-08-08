from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []

        def back(co, cc):
            if co == cc == n:
                return res.append("".join(s))
            if co < n:
                s.append('(')
                back(co + 1, cc)
                s.pop()
            if co > cc:
                s.append(')')
                back(co, cc + 1)
                s.pop()

        back(0, 0)
        return res


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
