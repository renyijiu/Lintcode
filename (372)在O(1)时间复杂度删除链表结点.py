'''
给定一个单链表中的表头和一个等待被删除的节点(非表头或表尾)。请在在O(1)时间复杂度删除该链表节点。并在删除该节点后，返回表头。

思路：O(1)时间意味着直接对待删除节点进行操作，将待删除节点的下一个节点的值赋给待删除节点，然后待删除节点的next指向下一节点的next（即待删节点.next.next），这样间接的删除了节点。
'''


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    # @param node: the node in the list should be deleted
    # @return: nothing
    def deleteNode(self, node):
        # write your code here
        if node is None:
            return False
        else:
            node.val = node.next.val
            node.next = node.next.next
