'''
给出一棵二叉树,返回其中序遍历.

思路：中序遍历为左结点，根，右结点
(1)递归解法：先递归遍历左结点，然后输出结点值，在递归遍历右结点。
(2)非递归解法：当结点不为空时，将结点入栈，将结点置为左孩子作为当前结点；若结点为空，则将栈顶元素出栈作为当前结点，输出结点值；再将结点置为右孩子作为当前结点，直至栈和结点均为空，表明全部遍历了。
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
    @return: Inorder in ArrayList which contains node values.
    """
    result = []
    def inorderTraversal(self, root):
        # write your code here
        if root is None:
            return self.result
        if root.left:              #左结点的递归
            self.inorderTraversal(root.left)
        self.result.append(root.val)
        if root.right:             #右结点的递归
            self.inorderTraversal(root.right)
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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        temp = []
        result = []
        while root or temp:
            if root:
                temp.append(root)
                root = root.left
            else:
                root = temp.pop()
                result.append(root.val)
                root = root.right
        return result
