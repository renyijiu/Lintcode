'''
给出一棵二叉树,返回其中序遍历.

思路：中序遍历顺序为左节点，根，右节点
(1)递归解法：先递归遍历左节点，然后输出根节点，在递归遍历右节点。
(2)非递归解法：当节点不为空时，将节点入栈，将节点置为左孩子作为当前节点；若节点为空，则将栈顶元素出栈作为当前节点，输出节点值；再将节点置为右孩子作为当前节点，直至栈和节点均为空，表明全部遍历了。
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
        if root.left:              #左节点的递归
            self.inorderTraversal(root.left)
        self.result.append(root.val)
        if root.right:             #右节点的递归
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
