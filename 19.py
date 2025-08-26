# medium
# 19. 从前序和中序遍历序列构造二叉树
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        # 前序遍历的第一个节点就是根节点
        root = TreeNode(preorder[0])
        
        # 在中序遍历中找到根节点的位置
        mid = inorder.index(preorder[0])
        
        # 递归构建左子树和右子树
        # 左子树：前序遍历[1:mid+1]，中序遍历[:mid]
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # 右子树：前序遍历[mid+1:]，中序遍历[mid+1:]
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
        