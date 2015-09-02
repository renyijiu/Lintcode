'''
给出一棵二叉树，返回其节点值的前序遍历。

思路：前序遍历：先输出根结点，再输出左结点，最后输出右结点。
     (1)递归解法：输出根结点，再递归遍历左结点，然后递归遍历右结点。
     (2)非递归遍历：先输出根结点值，在将结点入栈，将结点置为左孩子作为当前结点；当结点为空时，将栈顶元素出栈作为当前结点，并将结点置为右孩子作为当前结点；直到结点和栈均为空时，结束循环。 
'''


#递归解法
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
    @return: Preorder in ArrayList which contains node values.
    """
    result = []
    def preorderTraversal(self, root):
        # write your code here
        if root is None:
            return self.result
        self.result.append(root.val)
        if root.left:          #左结点的递归
            self.preorderTraversal(root.left)
        if root.right:         #右结点的递归
            self.preorderTraversal(root.right)
        return self.result
        

#非递归解法
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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        temp = []
        result = []
        while root or temp:
            if root:
                result.append(root.val)
                temp.append(root)
                root = root.left
            else:
                root = temp.pop()
                root = root.right
        return result
