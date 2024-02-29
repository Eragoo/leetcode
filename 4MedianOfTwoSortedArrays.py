from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            i = l + r // 2
            j = half - i - 2

            aL = A[i] if i >= 0 else float("-infinity")
            bL = B[j] if i >= 0 else float("-infinity")

            aR = A[i+1] if i + 1 <= len(A) - 1 else float("infinity")
            bR = B[j+1] if i + 1 <= len(B) - 1 else float("infinity")

            if aL <= bR and aR >= bL:
                if total % 2 == 0:
                    return (max(aL, bL) + min(aR, bR)) / 2
                else:
                    return min(aR, bR)
            elif aL > bR:
                r = i - 1
            else:
                l = i + 1


if __name__ == '__main__':
    # print(Solution().findMedianSortedArrays([1, 2, 3, 4], [1, 2, 5]))
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
    # print(Solution().findMedianSortedArrays([], [4]))
    # print(Solution().findMedianSortedArrays([1,3], [2,7]))
    # print(Solution().findMedianSortedArrays([], [2, 3]) == 2.5)
    # print(Solution().findMedianSortedArrays([3], [-2, -1]))
