'''
给一个01矩阵，求不同的岛屿的个数。
0代表海，1代表岛，如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。

思路：对二维矩阵进行遍历，初始化计数值，遇到1时，计数值加1,并对1周围的位置进行遍历，若为1则置为0(只需要考虑上下左右的位置），直至整个矩阵遍历完，返回计数值即可。
'''


class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        if not grid:
            return 0
        count = 0
        row = len(grid)
        col = len(grid[0])
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == 1:
                    count += 1
                    self.dfs(grid, i, j)
        return count
    
    def dfs(self, array, i, j):
        row = len(array)
        col = len(array[0])
        if i < 0 or i >= row or j < 0 or j >= col or array[i][j] != 1:
            return False
        array[i][j] = 0
        self.dfs(array, i-1, j)
        self.dfs(array, i+1, j)
        self.dfs(array, i, j-1)
        self.dfs(array, i, j+1)
