'''
给出若干闭合区间，合并所有重叠的部分。

思路：对区间按照start元素进行排序，然后就对区间数组进行遍历，比较相邻元素的区间重合度，不变或者使用新的去间代替两个旧区间。
'''


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        # write your code here
        if len(intervals) <= 1:
            return intervals
        else:
            length = len(intervals)
            i = 0
            intervals.sort(key = lambda x:x.start)
            while i < length-1:
                if intervals[i+1].start > intervals[i].end:
                    i += 1
                else:
                    if intervals[i+1].end <= intervals[i].end:
                        intervals.pop(i+1)
                        length -= 1
                    else:
                        intervals[i].end = intervals[i+1].end
                        intervals.pop(i+1)
                        length -= 1
            return intervals
