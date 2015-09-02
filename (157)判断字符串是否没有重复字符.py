'''
实现一个算法确定字符串中的字符是否均唯一出现.

思路：这个题解法也较多，思路较简单的是将字符串进行排序，然后判断相邻字符是否相等。
'''


class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        B = sorted(str)
        length = len(B)
        for i in range(0, length-1):
            if B[i] == B[i+1]:
                return False
        return True
