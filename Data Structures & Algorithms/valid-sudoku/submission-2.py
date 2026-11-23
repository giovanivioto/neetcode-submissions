class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## O(n^2) time
        ## O(n^2) space
        ## n = number if rows in the square grid
        slot_line = [{} for _ in range(len(board))]
        slot_column = [{} for _ in range(len(board))]
        slot_square = [{} for _ in range(len(board))]
        for line, x in enumerate(board):
            for column, value in enumerate(x):
                ##Line verification
                if value == '.':
                    continue
                if value not in slot_line[line]:
                    slot_line[line][value] = 0
                slot_line[line][value] += 1
                if slot_line[line][value] > 1:
                    return False

                ##Column verification
                if value not in slot_column[column]:
                    slot_column[column][value] = 0
                slot_column[column][value] += 1
                if slot_column[column][value] > 1:
                    return False

                ##Square verification
                square = int((line // 3) * 3 + (column // 3))
                if value not in slot_square[square]:
                    slot_square[square][value] = 0
                slot_square[square][value] += 1
                if slot_square[square][value] > 1:
                    return False
        return True
