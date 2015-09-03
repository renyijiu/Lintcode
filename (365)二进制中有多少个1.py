'''
计算在一个 32 位的整数的二进制表式中有多少个 1.

思路：网上这个题的解法有多种，但这种解法是比较高效和简洁的。n-1可以将n最后一个1消去，具体原理可以自己演算理解。
'''


class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        count = 0
        while(num != 0):
            num = num&(num-1)
            count += 1
        return count
        
        
#下面的是一种位右移的解法，也可以将1左移进行求解，代码较为类似
class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        count = 0
        while(num != 0):
            if (num & 1) == 1:
                count += 1
            num = num >>1
        return count
