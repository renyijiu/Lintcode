'''
给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。
不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。

思路：因为数组是排序的，对数组进行一遍遍历，比较A[i]和A[i+1]的值，若一致，则删除一个其中一个；若不一致，则向后移动，直到遍历完成。
'''


class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if len(A) < 2:
            return len(A)
        else:
            i=0
            while(i < (len(A)-1)):
                if A[i] == A[i+1]:
                    A.remove(A[i])
                else:
                    i += 1
            return len(A)
