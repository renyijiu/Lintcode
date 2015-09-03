'''
给定一个整数数组，找到和为零的子数组。你的代码应该返回满足要求的子数组的起始位置和结束位置。

思路：简单方法是使用双重循环，对已遍历数组元素求和，若和为0,则返回子数组的起始下标和结束下标。
'''


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        if len(nums) <= 0:
            return False
        elif len(nums) == 1:
            if nums[0] == 0:
                return [0,0]
            else:
                return False
        else:
            result = []
            for i in xrange(0, len(nums)):
                sub = 0
                j = i
                while(j < len(nums)):
                    sub += nums[j]
                    if sub == 0:
                        return [i, j]
                    j += 1
