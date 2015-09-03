'''
给定一个旋转排序数组，在原地恢复其排序。

思路：因为数组原本是有序的，所以对数组遍历时，若某个数小于前一个数，这代表着这是原本数组的起始位置，我们调整下输出顺序即可；若没有这种数，则代表着这个数组已经是有序的，直接输出即可。
'''


class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if len(nums) <= 0:
            return False
        elif len(nums) == 1:
            return nums
        else:
            i = 0
            while(i < (len(nums)-1)):
                if nums[i] > nums[i+1]:
                    nums[0:] = nums[i+1:]+nums[0:i+1]
                else:
                    i += 1
            return nums
