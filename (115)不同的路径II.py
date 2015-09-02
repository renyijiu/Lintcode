'''
跟进“不同的路径”：现在考虑网格中有障碍物，那样将会有多少条不同的路径？网格中的障碍和空位置分别用1和0来表示。

思路：和“不同的路径”类似，但这里我们采用循环的方式，先创建一个和路径数据一样的二维数组result[][]来记录由起点出发到当前结点的路径数，不一样的是当路径数组的值为1时，我们将对应位置的result置为0,表明障碍没有路径可达（需要设定初始行和列的值），循环获得这个数据的路径数，返回要求位置的值即可。
'''


class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if row <= 0 or col <= 0:
            return 0
        step = [[0 for _ in xrange(col)] for _ in xrange(row)]
        if obstacleGrid[0][0] == 0:
            step[0][0] = 1
        else:
            return 0
        for i in xrange(1, col):
            if obstacleGrid[0][i] != 1 and step[0][i-1] == 1:
                step[0][i] = 1
            else:
                step[0][i] = 0
        for i in xrange(1, row):
            if obstacleGrid[i][0] != 1 and step[i-1][0] == 1:
                step[i][0] = 1
            else:
                step[i][0] = 0
        for i in xrange(1, row):
            for j in xrange(1, col):
                if obstacleGrid[i][j] != 1:
                    step[i][j] = step[i-1][j] + step[i][j-1]
                else:
                    step[i][j] = 0
        return step[row-1][col-1]
