class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        w = 0
        used = k
        i = 0
        best = 0
        while i + w < len(s):
            ch = s[i]
            if ch == s[i + w]:
                w += 1
            elif used > 0:
                used -= 1
                w += 1
            else:
                used = k
                if best < w:
                    best = w
                w = 1
                i += 1
        return max(best, w)


def test(s, k, expected):
    r = Solution().characterReplacement(s, k)
    print("Resp: ", r, " Expected: ", expected)
    print("Pass: ", r == expected)
    print("--------------------------------")


if __name__ == '__main__':
    # test("ABAB", 2, 4)
    # test("AABABBA", 1, 4)
    # test("AACCA", 1, 3)
    # не міняє перший елемент, треба походу йти з центру
    test("ABBB", 2, 4)
