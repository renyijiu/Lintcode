'''
合并两个排序的整数数组A和B变成一个新的数组。

思路：这个和“合并排序数组”的区别是，A数组中含有一些空元素，当A和B直接合并排序输出时，因为A后面的空元素会导致结果出错，自己尝试了多次才发现问题；所以这里换种思路，因为A数组大小为m+n，包含了B的大小，所以将B中的值倒序复制到A的后面，使A成为一个包含A和B元素的完整数组，然后再排序输出。
'''


class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        if len(A) == 0 and len(B) == 0:
            return False
        elif len(A) == 0:
            return B
        elif len(B) == 0:
            return A
        else:
            k = m + n - 1
            temp = n - 1
            while(temp >= 0):
                A[k] = B[temp]
                k -= 1
                temp -= 1
            A.sort()
            return A
