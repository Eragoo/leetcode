class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(i for i in s if (ord(i) > 96 and ord(i) < 123) or (ord(i) > 47 and ord(i) < 58)).lower()
        l = 0
        r = len(s) - 1
        if len(s) == 0:
            return True
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1
        return l >= r


if __name__ == '__main__':
    print(Solution().isPalindrome("A man, a plan, a canal: Panama") == True)
    print(Solution().isPalindrome("race a car") == False)
    print(Solution().isPalindrome(" ") == True)
    print(Solution().isPalindrome("0P") == False)
    print(Solution().isPalindrome("a") == True)
