Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.m=0
        def dfs(root):
            if root==None:return 0
            
            left_height=dfs(root.left)
            right_height=dfs(root.right)
            self.m=max(self.m,left_height+right_height)
            return (max(left_height,right_height)+1)
        dfs(root)
        return ((self.m))
            