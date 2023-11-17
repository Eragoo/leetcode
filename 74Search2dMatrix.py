from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_s = 0
        n = len(matrix) - 1
        m = len(matrix[0]) - 1
        r_e = n

        i = 0
        set_i = False
        while r_s <= r_e:
            pivot = int(r_s + (r_e - r_s) / 2)
            l_c = matrix[pivot][0]
            r_c = matrix[pivot][m]

            if l_c == target or r_c == target:
                return True
            if l_c < target < r_c:
                i = pivot
                set_i = True
                break
            if l_c > target:
                r_e = pivot - 1
            if r_c < target:
                r_s = pivot + 1

        if not set_i:
            return False

        start = 0
        end = len(matrix[i])

        if len(matrix[i]) == 1:
            return matrix[i][0] == target

        while start < end:
            pivot = int(start + ((end - start) / 2))
            el = matrix[i][pivot]
            if el == target:
                return True
            elif el > target:
                end = pivot - 1
            elif el < target:
                start = pivot + 1

        return matrix[i][end] == target


if __name__ == '__main__':
    print(Solution().searchMatrix([[1]], 1))