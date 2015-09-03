'''
给一个排序数组（从小到大），将其转换为一棵高度最小的排序二叉树。

思路：当二叉树的高度最小时，意味着这个二叉树应该是最接近二叉平衡树的状态的，这代表着左右子树的节点个数最接近。所以我们将数组中间位置作为二叉树的根节点，最左右子树做相同递归，最后返回树。
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
    @param A: a list of integer
    @return: a tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here
        if len(A) <= 0:
            return None
        return self.recursion(A, 0, len(A)-1)
        
    def recursion(self, array, start, end):
        if start <= end:
            mid = (start+end) / 2
            root = TreeNode(array[mid])
            root.left = self.recursion(array, start, mid-1)
            root.right = self.recursion(array, mid+1, end)
            return root
