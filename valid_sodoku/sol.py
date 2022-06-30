from collections import defaultdict
def isValidSudoku(board):
    rows=defaultdict(set)
    columns=defaultdict(set)
    boxes=defaultdict(set)
        
    for r,row in enumerate(board):
        for c,column in enumerate(row):
            print(c)
            print
            if row[c]==".":
                continue
            if row[c] in columns[c] or row[c] in rows[r] or row[c] in boxes[(r//3,c//3)]:
                 return False
            rows[r].add(row[c])
            columns[c].add(row[c])
            boxes[((r//3,c//3))].add(row[c])
    return True
print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))