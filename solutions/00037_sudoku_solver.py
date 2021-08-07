from typing import List


class Solution:
    def solveSudoku(self, s_board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        board: List[List[int]] = list(map(lambda row: list(map(lambda item: 0 if item == "." else int(item), row)), s_board))

        def possibilities_for_row(i) -> set:
            nonlocal board
            result = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            for j in range(9):
                if board[i][j] != 0:
                    result.remove(board[i][j])
            return result

        def possibilities_for_col(j):
            nonlocal board
            result = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            for i in range(9):
                if board[i][j] != 0:
                    result.remove(board[i][j])
            return result

        def possibilities_for_box(i0, j0):
            nonlocal board
            result = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            delta_i = 3 * i0
            delta_j = 3 * j0
            for i in range(3):
                for j in range(3):
                    if board[delta_i + i][delta_j + j] != 0:
                        result.remove(board[delta_i + i][delta_j + j])
            return result

        def possibilities_for_cell(i, j):
            return possibilities_for_row(i).intersection(possibilities_for_col(j)).intersection(possibilities_for_box(i // 3, j // 3))

        solved = False

        def solve_sudoku():
            nonlocal solved
            nonlocal s_board
            nonlocal board

            if solved:
                return

            i0 = None
            j0 = None

            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        i0 = i
                        j0 = j



            if i0 is None:
                solved = True
                for i in range(9):
                    for j in range(9):
                        s_board[i][j] = "." if board[i][j] == 0 else str(board[i][j])
                # print(board)
                return

            possibilities = possibilities_for_cell(i0, j0)
            for value in possibilities:
                board[i0][j0] = value
                solve_sudoku()
                board[i0][j0] = 0

        solve_sudoku()





s = Solution()
a = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
s.solveSudoku(a)
print(a)