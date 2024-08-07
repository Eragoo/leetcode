class Solution:
    def isValid(self, s: str) -> bool:
        r = []
        for e in s:
            if e in [']', '}', ')']:
                if len(r) == 0 or (len(r) >= 0 and abs(ord(r.pop()) - ord(e)) > 2):
                    return False
            else:
                r.append(e)
        return len(r) == 0

# {[]}
if __name__ == '__main__':
    print(Solution().isValid("([}}])"))
    print(Solution().isValid("[)"))
    print(Solution().isValid(")"))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("({{}}[]())"))
