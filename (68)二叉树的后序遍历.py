'''
给出一棵二叉树，返回其节点值的后序遍历。

思路：后序遍历：遍历顺序为左结点，右结点，根
     (1)递归方法：先递归遍历左结点，再递归遍历右结点，然后输出根结点
     (2)非递归方法：这个和前序和中序的方法类似，但区别是根结点的输出是排在左右子树都遍历完的时候的，不能直接就出栈，所以需要加一个出栈判断，当右子树遍历完成时，这表明可以将根结点出栈了。
'''


#递归方法
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
    @return: Postorder in ArrayList which contains node values.
    """
    result = []
    def postorderTraversal(self, root):
        # write your code here
        if root is None:
            return self.result
        if root.left:                  
            self.postorderTraversal(root.left)
        if root.right:
            self.postorderTraversal(root.right)
        self.result.append(root.val)
        return self.result
        
        
        
#非递归的方法
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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        temp = []
        result = []
        pre = None
        while root or temp:
            if root:
                temp.append(root)
                root = root.left
            elif temp[-1].right != pre:
                root = temp[-1].right
                pre = None
            else:
                pre = temp.pop()
                result.append(pre.val)
        return result
