'''
给定一个排序链表，删除所有重复的元素每个元素只留下一个。

思路：因为链表是排序的，所以只需要比较邻近的两个结点的值是否一样就可以了，注意链表结束的判断！
'''


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        result = head
        if not head or not head.next:
            return head
        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return result
