'''
给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。该数字按照大小进行排列，最大的数在列表的最前面。

思路：将数字数组转换成整数，然后求得加一的值，将这个值转换成数字数组，最大的数在数组的前面(采用倒序一下就可以了)
'''


class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        char = []
        length = len(digits)
        num = 0
        for i in range(0, length):
            num += digits[i]*(10**(length-1-i))
        num += 1
        while(num != 0):
            temp = num % 10
            char.append(temp)
            num /= 10
        char.reverse()
        return char
