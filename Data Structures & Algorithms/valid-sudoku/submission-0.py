class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # every row check if duplicate
        # every column check for duplicate
        column = defaultdict(set)
        squares = defaultdict(set)
        for i, row in enumerate(board):
            rowCount = set()
            for t, box in enumerate(row):
                if box == '.':
                    continue
                elif box in rowCount:
                    return False
                else:
                    rowCount.add(box)
                if box in column[t]:
                    return False
                else:
                    column[t].add(box)
                
                square = (i // 3, t // 3)
                if box in squares[square]:
                    return False
                else:
                    squares[square].add(box)
                
        return True


        