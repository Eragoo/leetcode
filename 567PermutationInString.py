class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1a = {}
        s2a = {}

        for i in range(len(s1)):
            s1a[s1[i]] = s1a.get(s1[i], 0) + 1


        i = 0
        j = len(s1) - 1
        for z in range(i, j+1):
            s2a[s2[z]] = s2a.get(s2[z], 0) + 1

        if s1a == s2a:
            return True

        j+=1
        while j < len(s2):
            s2a[s2[j]] = s2a.get(s2[j], 0) + 1
            if s2a.get(s2[i], 0) > 1:
                s2a[s2[i]] = s2a.get(s2[i], 0) - 1
            else:
                s2a.pop(s2[i])

            if s1a == s2a:
                return True

            i+=1
            j+=1

        return False


def test(s1, s2, expected):
    print("S1: " + s1 + " S2: " + s2)
    print(Solution().checkInclusion(s1, s2) == expected)
    print("--------------------------------------")

if __name__ == '__main__':
    test("ab", "afgsb", False)
    test("ab", "eidboaoo", False)
    test("ab", "eidbaoo", True)
