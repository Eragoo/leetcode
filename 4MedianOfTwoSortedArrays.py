from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            if len(nums2) % 2 == 0:
                return nums2[(len(nums2) - 1) // 2] + nums2[((len(nums2) - 1) // 2) - 1];
            else:
                return nums2[(len(nums2) - 1) // 2]

        if len(nums2) == 0:
            if len(nums1) % 2 == 0:
                return nums1[(len(nums1) - 1) // 2] + nums1[((len(nums1) - 1) // 2) - 1];
            else:
                return nums1[(len(nums1) - 1) // 2]

        l = 0
        r = len(nums1) - 1
        total = len(nums1) + len(nums2)
        while l <= r:
            mid = (l + r) // 2
            mid2 = (total // 2) - (mid + 1) - 1

            if mid + 1 > len(nums1) - 1 and mid2 < 0:
                return (nums1[len(nums1) - 1] + nums2[0]) / 2

            if nums1[mid] <= nums2[mid2 + 1] and nums2[mid2] <= nums1[mid + 1]:
                if (total % 2) == 0:
                    return (nums1[mid + 1] + nums2[mid2 + 1]) / 2
                else:
                    return min(nums1[mid + 1], nums2[mid2 + 1])
            else:
                l = mid + 1


if __name__ == '__main__':
    # print(Solution().findMedianSortedArrays([1, 2, 3, 4], [1, 2, 5]))
    # print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
    # print(Solution().findMedianSortedArrays([], [4]))
    print(Solution().findMedianSortedArrays([1,3], [2,7]))
