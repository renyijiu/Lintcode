'''
给出一个不含重复数字的排列，求这些数字的所有排列按字典序排序后该排列的编号。其中，编号从1开始。

思路：对于排列的计算其实是一个阶乘的计算。对数组排序，用于确定在目标排列之前存在多少种可能，然后对于后续排列使用阶乘计算全部的排列数。
'''


class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndex(self, A):
        # Write your code here
        if len(A) <= 0:
            return False
        elif len(A) == 1:
            return 1
        else:
            temp = sorted(A)
            sub = 0
            for i in xrange(0, len(A)):
                count = 1
                for j in xrange(0,len(temp)):
                    if A[i] == temp[j]:
                        break
                    count += 1
                sub += (count-1)*(self.f(len(temp)-1))
                temp.remove(A[i])
            return sub+1
            
    def f(self, n, acc=1):       #阶乘计算
        if n == 0:
            return acc
        return self.f(n-1, acc*n)
