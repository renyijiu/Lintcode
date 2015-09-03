'''
给定一个二叉树，找出其最小深度。二叉树的最小深度为根节点到最近叶子节点的距离。

思路：和“二叉树的最大深度”极为相似，同样遍历左子树和右子树然后返回深度值较小的那个即可，但这里需要考虑下，当根的左子树或者右子树为空时，深度为非空子树的最小深度，而不是0，所以需要考虑特殊值的处理。
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
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def minDepth(self, root):
        # write your code here
        return self.recursion(root, 0)
        
    def recursion(self, root, depth):
        if not root:
            return depth
        elif root.left is None and root.right:
            return self.recursion(root.right, depth+1)
        elif root.left and root.right is None:
            return self.recursion(root.left, depth+1)
        else:
            return min(self.recursion(root.left, depth+1), self.recursion(root.right, depth+1))
