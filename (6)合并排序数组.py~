'''
合并两个排序的整数数组A和B变成一个新的数组。

思路：这题解法其实也挺多样的，可以类似“排序链表的合并”去解决；这里采用python的sort函数直接求解，将A和B合并，排序后输出解
'''


class Solution:
    # @param A and B: sorted integer array A and B.
    # @return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        if len(A) == 0 and len(B) == 0:
            return False
        elif len(A) == 0:
            return B
        elif len(B) == 0:
            return A
        else:
            A.extend(B)
            return sorted(A)
