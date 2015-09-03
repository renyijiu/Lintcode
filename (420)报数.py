'''
报数指的是，按照其中的整数的顺序进行报数，然后得到下一个数。如下所示：
1, 11, 21, 1211, 111221, ...
1 读作 "one 1" -> 11.
11 读作 "two 1s" -> 21.
21 读作 "one 2, then one 1" -> 1211.
给定一个整数 n, 返回 第 n 个顺序。

思路：题目理解了就比较简单，遍历字符串，使用计数值对一类字符个数进行计算，然后与字符形成一个新的字符串。这里我们采用从后向前对字符串进行遍历，用计数值对相同字符计算个数，如此遍历完字符串生成一个新的字符串。
'''


class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        # Write your code here
        string = '1'
        for _ in xrange(n-1):
            count = 0
            temp = string[-1]
            result = ''
            for i in xrange(len(string)-1, -1, -1):
                if temp == string[i]:
                    count += 1
                else:
                    result = str(count) + temp + result
                    temp = string[i]
                    count = 1
            string = str(count) + temp + result
        return string
