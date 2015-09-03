'''
跟进“删除重复数字”，如果可以允许出现两次重复将如何处理？

思路：过程和“删除重复数字”一样，只是增加一个计数值用来判断重复数字是否超过了两次，从来确定是否删除这个元素。
'''


class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        i = 0
        count = 1
        if len(A) <= 2:
            return len(A)
        else:
            while(i < len(A)-1):
                if A[i] == A[i+1]:
                    if count < 2:
                        count += 1
                        i += 1
                    else:
                        A.remove(A[i])
                else:
                    count = 1
                    i += 1
