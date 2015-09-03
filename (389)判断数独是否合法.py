'''
请判定一个数独是否有效。该数独可能只填充了部分数字，其中缺少的数字用 . 表示。

思路：判断是否合法需要判断数独的每一行、每一列、9个小的九宫格中是否存在重复的数字。若每种情况均循环判断，则需要对整个二维数组遍历三次，还可以对此再优化；整个二维数组遍历一遍，对三种情况在循环中单独判断，而行和列的判断的判断较为简单，9个小的九宫格的遍历需要考虑下，对于(i/3*3+j/3)和(i%3*3+j%3)这两个编写需要思考下，比较巧妙的编写！
'''


class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in xrange(9):
            row = []
            col = []
            square = []
            for j in xrange(9):
                try:
                    row_element = int(board[i][j])
                    if row_element in row:
                        return False
                    else:
                        row.append(row_element)
                except:
                    pass
                
                try:
                    col_element = int(board[j][i])
                    if col_element in col:
                        return False
                    else:
                        col.append(col_element)
                except:
                    pass
                
                try:
                    square_element = int(board[i/3*3 + j/3][i%3*3 + j%3])
                    if square_element in square:
                        return False
                    else:
                        square.append(square_element)
                except:
                    pass
        return True
