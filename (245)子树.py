'''
有两个不同大小的二进制树： T1 有上百万的节点； T2 有好几百的节点。请设计一种算法，判定 T2 是否为 T1的子树。

思路：先在T1中递归匹配和T2根节点相等的节点，待找到节点后，对T1和T2同时进行递归进行子树的匹配，当递归结束时若为真，则返回True，若最后没有匹配，返回False。(可以分成两个模块，在主函数中递归寻找匹配的根节点，在自定义函数中进行子树的匹配)
'''


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        # write your code here
        if self.tree_match(T1, T2):
            return True
        if T1 is None:
            return False
        return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2) 
            
    def tree_match(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if None in [t1, t2] or t1.val != t2.val:
            return False
        return self.tree_match(t1.left, t2.left) and self.tree_match(t1.right, t2.right)
