'''
写出一个函数 anagram(s, t) 去判断两个字符串是否是颠倒字母顺序构成的.

思路：将两个字符串进行排序然后进行比较判断，若一致则一样，否则False；这个思路较简单，其他方法注意考虑边界值的判断
'''


class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        if s == '' and t == '':
            return True
        else:
            A = sorted(list(s))
            B = sorted(list(t))
            if A == B:
                return True
            else:
                return False
