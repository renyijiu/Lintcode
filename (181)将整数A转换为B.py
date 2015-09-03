'''
如果要将整数A转换为B，需要改变多少个bit位？

思路：首先通过将A和B进行异或，确定两者不同的比特位，然后通过对异或结果进行二进制1的计数确定不同的位数即可。
'''


class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        count = 0
        c = a ^ b
        if c < 0:
            c = ~c
            while(c):
                c &= (c-1)
                count += 1
            return (32 - count)
        else:
            while(c):
                c &= (c-1)
                count += 1
            return count
