'''
给定一个数组和一个值，在原地删除与值相同的数字，返回新数组的长度。元素的顺序可以改变，并且对新的数组不会有影响。

思路：对数组进行一遍遍历，若数字在数组中，则从数组中删除，若不存在则跳过，最后返回新数组。
'''


#解法1
class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        while True:
            if elem in A:
                A.remove(elem)
            else:
                break
        return A
        
        
#解法2
class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        i = 0
        while i < len(A):
            if elem == A[i]:
                A.remove(elem)
            else:
                i += 1
        return A
