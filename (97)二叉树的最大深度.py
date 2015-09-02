'''
给定一个二叉树，找出其最大深度。二叉树的深度为根节点到最远叶子节点的距离。

思路：这类题需要遍历整棵树才能确定最大深度，所以使用递归的方法较为简单。对左子树和右子树进行递归遍历，返回深度值较大的那个即可！
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
    def maxDepth(self, root):
        # write your code here
        return self.recursion(root, 0)
        
    def recursion(self, root, depth):
        if not root:
            return depth
        return max(self.recursion(root.left, depth+1), self.recursion(root.right, depth+1))
