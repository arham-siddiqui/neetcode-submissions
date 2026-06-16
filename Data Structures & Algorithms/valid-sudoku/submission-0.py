class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowDup = collections.defaultdict(set)
        colDup = collections.defaultdict(set)
        squareDup = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if (board[r][c] in rowDup[r]) or (board[r][c] in colDup[c]) or (board[r][c] in squareDup[(r//3, c//3)]):
                    return False
                
                rowDup[r].add(board[r][c])
                colDup[c].add(board[r][c])
                squareDup[(r//3, c//3)].add(board[r][c])
        
        return True
        

        

                
            
