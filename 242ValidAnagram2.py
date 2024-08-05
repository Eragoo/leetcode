class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = dict()
        d2 = dict()
        for i in range(0, len(s)):
            a1 = s[i]
            a2 = t[i]
            d1[a1] = d1.get(a1, 0) + 1
            d2[a2] = d2.get(a2, 0) + 1

        return d1 == d2


if __name__ == '__main__':
    print(Solution().isAnagram("anagram","nagaram") == True)
    print(Solution().isAnagram("rat", "car") == False)