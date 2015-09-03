'''
给出一个无重叠的按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

思路：将新区间插入到区间列表中形成一个新的列表，按照起始元素排序，然后按照“合并区间”的方法，对列表遍历，判断相邻区间的重合度，若有重合，用新的区间代替两个旧区间，若无，向后遍历。（其实较好的解法是因为原列表已经有序，直接在插入时对两区间进行判断，减少操作量,但代码复杂度上升）
'''


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        results = []
        i = 0
        # write your code here
        results = intervals
        if newInterval:
            results.append(newInterval)
        length = len(results)
        if length <= 1:
            return results
        results.sort(key=lambda x: x.start)
        while i < length-1:
            if intervals[i+1].start > intervals[i].end:
                i += 1
            else:
                if intervals[i+1].end <= intervals[i].end:
                    results.pop(i+1)
                    length -= 1
                else:
                    intervals[i].end = intervals[i+1].end
                    results.pop(i+1)
                    length -= 1
        return results
