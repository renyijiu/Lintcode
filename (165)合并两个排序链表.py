'''
将两个排序链表合并为一个新的排序链表

思路：创建一个新的链表，设置两个指针指向两个链表头，对指针指向的两个值进行比较，选取小的将值插入新链表，并将指针向后移动一位，重复上述过程，直至两个链表均遍历过了结束，返回新链表。(考虑清楚当有一个链表为空时的特殊情况)
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
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        resultHead = ListNode(None)
        cur1 = l1
        cur2 = l2
        cur = resultHead
        while cur1 or cur2:
            if not cur1:
                cur.val = cur2.val
                cur2 = cur2.next
            elif not cur2:
                cur.val = cur1.val
                cur1 = cur1.next
            else:
                if cur1.val <= cur2.val:
                    cur.val = cur1.val
                    cur1 = cur1.next
                else:
                    cur.val = cur2.val
                    cur2 = cur2.next
            if cur1 or cur2:
                cur.next = ListNode(None)
                cur = cur.next
        return resultHead
