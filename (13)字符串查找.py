'''
字符串查找（又称查找子字符串），是字符串操作中一个很有用的函数。你的任务是实现这个函数。
对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。
如果不存在，则返回 -1。

思路：o(n^2)的算法，类似于“子树”的判断，先匹配出首字母相等的位置，在进行字符串的匹配判断，若相等返回位置；若不相等，则回溯继续进行首字母的匹配。
     o(n)的算法，对于上面的方法进行优化，对不匹配的回溯过程优化，可以查找资料学习，如KMP算法。
     这道题有个简单的算法，就是利用python的find函数直接进行判断。
'''   

     
class Solution:
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        else:
            return source.find(target)
