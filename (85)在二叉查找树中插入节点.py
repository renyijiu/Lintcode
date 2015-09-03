'''
给定一棵二叉查找树和一个新的树节点，将节点插入到树中。你需要保证该树仍然是一棵二叉查找树。

思路：将节点的值和根的值进行比较，若大于则将根置为左孩子作为当前节点，若小于或等于将右孩子作为当前节点；循环遍历直至找到需要插入节点的位置，返回新的树即可。
'''


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if not root:
            return node
        else:
            cur = root
            while cur:
                if node.val > cur.val:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = node
                        return root
                elif node.val < cur.val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = node
                        return root
                else:
                    return root
            return root
