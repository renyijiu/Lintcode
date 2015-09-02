'''
实现 int sqrt(int x) 函数，计算并返回 x 的平方根。

思路：题目要求时间复杂度为o(log(x)),则使用二分法即可。
'''


class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        low = 0
        high = x
        while low <= high:
            mid = (low + high) / 2
            if mid**2 > x:
                high = mid - 1
            elif mid**2 < x:
                if (mid+1)**2 > x:
                    return mid
                else:
                    low = mid + 1
            else:
                return mid   
