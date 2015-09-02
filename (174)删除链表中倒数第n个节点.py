'''
给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。

思路：若没有时间的要求，可以先对链表遍历一遍获得链表长度，在第二次遍历时获得倒数第n个元素；若要求只遍历一遍时，可以采用一个额外的计数指针temp，先让temp向前移动n-1，然后另一个指针从头节点开始，两个指针一起向后移动直至计数指针到达链表末尾，另一指针所指的节点即为倒数第n个节点，然后对这个节点进行删除操作即可(链表操作可以再查资料了解)。
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
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        temp = head
        result = head
        i = 0
        if not head.next or not head:
            return None
        if n == 1:
            while temp.next.next:
                temp = temp.next
            temp.next = None
            return head
        while i < n-1:
            temp = temp.next
            i += 1
        while temp.next:
            temp = temp.next
            result = result.next
        result.val = result.next.val
        result.next = result.next.next
        return head
