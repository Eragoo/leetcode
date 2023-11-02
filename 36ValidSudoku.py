from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            row_uniq = set()
            row_count = 0

            col_uniq = set()
            col_count = 0
            for j in range(0, 9):
                row_el = board[i][j]
                col_el = board[j][i]

                if row_el != ".":
                    row_uniq.add(row_el)
                    row_count += 1
                if col_el != ".":
                    col_uniq.add(col_el)
                    col_count += 1

                if len(row_uniq) < row_count or len(col_uniq) < col_count:
                    return False

        for bi in range(0, 3):
            for bj in range(0, 3):
                box_uniq = set()
                box_count = 0
                for i in range(0, 3):
                    for j in range(0, 3):
                        curr = board[(bi * 3)+i][(bj * 3)+j]

                        if curr != ".":
                            box_uniq.add(curr)
                            box_count += 1

                        if len(box_uniq) < box_count:
                            return False

        return True


if __name__ == '__main__':
    sudoku_1 = [[".", "8", "7", "6", "5", "4", "3", "2", "1"],
              ["2", ".", ".", ".", ".", ".", ".", ".", "."],
              ["3", ".", ".", ".", ".", ".", ".", ".", "."],
              ["4", ".", ".", ".", ".", ".", ".", ".", "."],
              ["5", ".", ".", ".", ".", ".", ".", ".", "."],
              ["6", ".", ".", ".", ".", ".", ".", ".", "."],
              ["7", ".", ".", ".", ".", ".", ".", ".", "."],
              ["8", ".", ".", ".", ".", ".", ".", ".", "."],
              ["9", ".", ".", ".", ".", ".", ".", ".", "."]]

    sudoku = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
              [".", "4", ".", "3", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", "3", ".", ".", "1"],
              ["8", ".", ".", ".", ".", ".", ".", "2", "."],
              [".", ".", "2", ".", "7", ".", ".", ".", "."],
              [".", "1", "5", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", "2", ".", ".", "."],
              [".", "2", ".", "9", ".", ".", ".", ".", "."],
              [".", ".", "4", ".", ".", ".", ".", ".", "."]]

    print(Solution().isValidSudoku(sudoku_1))
