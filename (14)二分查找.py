'''
给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。

思路：因为数组是排序的，所以直接使用二分查找就可以了，而且python对于大数据是支持的，所以挑战中的整数个数大于2**32这个并不需要考虑。
'''


class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        low = 0
        high = len(nums)-1
        while(low <= high):
            mid = (low + high) / 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                while(mid > 0 and (nums[mid] == nums[mid-1])):
                    mid -= 1
                return mid
        return -1
