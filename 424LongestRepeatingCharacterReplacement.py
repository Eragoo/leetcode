class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            if (r - l + 1) - max(count.values()) <= k:
                res = max(res, r - l + 1)
            else:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1

        return res

def test(s, k, expected):
    r = Solution().characterReplacement(s, k)
    print("Resp: ", r, " Expected: ", expected)
    print("Pass: ", r == expected)
    print("--------------------------------")


if __name__ == '__main__':
    test("ABAB", 2, 4)
    test("AABABBA", 1, 4)
    test("AACCA", 1, 3)
    # не міняє перший елемент, треба походу йти з центру
    test("ABBB", 2, 4)
    test("ABAA", 0, 2)
