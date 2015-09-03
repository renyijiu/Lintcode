'''
给定两个二进制字符串，返回他们的和（用二进制表示）。

思路：首先判断字符串是否为空的特殊情况，然后将两个字符串用int直接转成整数求和，再将和转为二进制数（PS：使用bin时输出值前面有'0b'符号，直接输出是会Wrong Answer,所以输出需要bin()[2:]提取二进制字符串）
'''


class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        if a is None and b is None:
            return False
        elif a is None:
            return b
        elif b is None:
            return a
        else:
            temp1 = int(a, 2)
            temp2 = int(b, 2)
            return bin(temp1+temp2)[2:]
