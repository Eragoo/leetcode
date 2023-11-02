from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    countS = [0] * 26
    for c in s:
        countS[ord(c) - ord("a")] += 1

    count = [0] * 26
    for c in t:
        count[ord(c) - ord("a")] += 1

    return countS == count





if __name__ == '__main__':
    print(isAnagram("anagram", "nagaram"))