'''
给定一个字符串s，将s分割成一些子串，使每个子串都是回文串。返回s所有可能的回文串分割方案。

思路：将字符串分成两个部分，当前半部分是回文串的时候在对后半部分进行判断，若是则将这种分类加入到结果中（判断字符串回文的办法可以采用递归的办法）。从头开始对字符串按上述的步骤遍历一遍即可。
'''


class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        result = []
        self.get_partition(s, [], result)
        return result
        
    def get_partition(self, str, cur, result):
        if not str:
            result.append(cur)
        for i in xrange(len(str)):
            if self.is_palindrome(str[:i+1]):
                self.get_partition(str[i+1:], cur+[str[:i+1]], result)
                
    def is_palindrome(self, str):
        return str == str[::-1]
