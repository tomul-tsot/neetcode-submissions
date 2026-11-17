class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
              
        columns=[[] for _ in range(9)]

        row1=board[0]
        row2=board[1]
        row3=board[2]
        row4=board[3]
        row5=board[4]
        row6=board[5]
        row7=board[6]
        row8=board[7]
        row9=board[8]  

        for i in range(9):
          
            columns[i].extend([row1[i],row2[i],row3[i],row4[i],row5[i],row6[i],row7[i],row8[i],row9[i]])
        

        
        b1 = row1[0:3] + row2[0:3] + row3[0:3] 
        b2 = row1[3:6] + row2[3:6] + row3[3:6]
        b3 = row1[6:9] + row2[6:9] + row3[6:9]
        b4 = row4[0:3] + row5[0:3] + row6[0:3]
        b5 = row4[3:6] + row5[3:6] + row6[3:6]
        b6 = row4[6:9] + row5[6:9] + row6[6:9]
        b7 = row7[0:3] + row8[0:3] + row9[0:3]
        b8 = row7[3:6] + row8[3:6] + row9[3:6]
        b9 = row7[6:9] + row8[6:9] + row9[6:9]
        
        boxes = [b1, b2, b3, b4, b5, b6, b7, b8, b9]


        for i in range(9):
            if len(list(x for x in board[i] if x!='.'))!=len(set(x for x in board[i] if x!='.')):
                return False
            if len(list(x for x in columns[i] if x!='.'))!=len(set(x for x in columns[i] if x!='.')):
                return False
            if len(list(x for x in boxes[i] if x!='.'))!=len(set(x for x in boxes[i] if x!='.')):
                return False
        return True
