'''
分割一个整数数组，使得奇数在前偶数在后。

思路：设置两个指针分别指向开始和结束位置，两个指针分别向中间移动，当前面指针遇到偶数，后面指针遇到奇数，两者对应位置交换值，然后继续上述过程当两指针重合时停止。
'''


class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        i = 0
        j = len(nums)-1
        while(i < j):
            if (nums[i] & 1 == 1):
                i += 1
            else:
                if nums[j] & 1 ==0:
                    j -= 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
