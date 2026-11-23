class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## O(n^2) time
        ## O(n^2) space
        ## n = number if rows in the square grid
        slot_line = [set() for _ in range(len(board))]
        slot_column = [set() for _ in range(len(board))]
        slot_square = [set() for _ in range(len(board))]
        for line, x in enumerate(board):
            for column, value in enumerate(x):
                #Verify if is digit
                if value == '.':
                    continue

                ##Line verification
                if value in slot_line[line]:
                    return False
                slot_line[line].add(value)

                ##Column verification
                if value in slot_column[column]:
                    return False
                slot_column[column].add(value)

                ##Square verification
                square = (line // 3) * 3 + (column // 3)
                if value in slot_square[square]:
                    return False
                slot_square[square].add(value)
        return True
