'''
设计一个算法，计算出n阶乘中尾部零的个数。

思路：使用传统的计算出阶乘的值，再算出值中0的个数，但当阶乘较大时，虽然python支持大数据，但依旧会超时；想要的得到有多少个0,等价于计算阶乘中有多少个10,而10是由5*2获得，5大于2,即只需要知道5的个数就可以判断出阶乘值有多少个0。
'''


class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        if n < 0:
            return False
        else:
            sub = 0
            while(n/5 != 0):
                temp = n/5
                sub += temp
                n = temp
            return sub
