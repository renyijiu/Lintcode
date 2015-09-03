'''
有一个机器人的位于一个M×N个网格左上角（下图中标记为'Start'）。机器人每一时刻只能向下或者向右移动一步。机器人试图达到网格的右下角（下图中标记为'Finish'）。问有多少条不同的路径？

思路：这其实是斐波纳契数列的一个变化，由最后一个分析，向下或者向右到达paths[m][n]，则路径数由paths[m][n] = paths[m-1][n] + paths[m][n-1]即可，现在问题简单了，采用递归或者循环即可解决。
'''


class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        paths = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or j == 0:
                    paths[i][j] = 1
                else:
                    paths[i][j] = paths[i][j-1]+paths[i-1][j]
        return paths[m-1][n-1]
