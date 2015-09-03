'''
用 O(1) 时间检测整数 n 是否是 2 的幂次。

思路：2的幂次转换成二进制数只有一个1,n-1可以将原本的1转换成0,并与n相与,若为0则可以保证n只有一个1。(这是位运算的巧妙应用)
'''


class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if (n > 0 and (n & (n-1) == 0)):
            return True
        else:
            return False
