class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        d = []
        par = {'[': ']', '(': ')', '{': '}'}

        for p in s:
            if p in ['[', '(', '{']:
                d.append(p)
            else:
                if len(d) > 0:
                    l = d.pop()
                    if par.get(l) != p:
                        return False
                else:
                    return False
        return len(d) == 0


if __name__ == '__main__':
    print(Solution().isValid(")"))
