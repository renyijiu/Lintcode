'''
给定一个未排序的整数数组，找到其中位数。中位数是排序后数组的中间值，如果数组的个数是偶数个，则返回排序后数组的第N/2个数。

思路：采用部分快排的方法，选取一个基数进行比较排序，将小于的数存放在lt数组，等于的数放在eq数组，大于的数存放在gt数组；这样就可以得出基数在整个数组中的位置，与中间值比较，判断出中间值在哪个数组，重复上面的步骤，直到基数值为中间值。
'''


class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        # write your code here
        if len(nums) == 0:
            return False
        elif len(nums) == 1:
            return nums[0]
        else:
            if len(nums) % 2 == 1:
                N = (len(nums)+1) / 2
            else:
                N = len(nums) / 2
            return self.quick_sort(nums, N)

    def quick_sort(self, arry, size):                 #修改的快速排序
        key = arry[0]
        lt = [i for i in arry if cmp(i, key) == -1]           #将元素分类，确定基数的位置     
        eq = [i for i in arry if cmp(i, key) == 0]
        gt = [i for i in arry if cmp(i, key) == 1]
        if (len(lt)+len(eq)) < size:
            size = size - len(lt+eq)
            return self.quick_sort(gt, size)
        elif size <= len(lt):
            return self.quick_sort(lt, size)
        else:
            return eq[0]
