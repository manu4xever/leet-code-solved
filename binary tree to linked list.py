# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        
        while root!=None:
            if root.left==None:
                root =root.right
            else:
                tmp=root.right
                root.right=root.left
                root.left=None
                root=root.right
                right=root
            if right.left !=None:    
                right = right.right
            right.right=tmp
#                 right=root
#                 if right.right!=None:
#                     right=right.right
#                     #root.left=None
#                 right.right = tmp
                

                
                
#         while root.left!=None:
#             root= tmp
#             root.left=None
#             root=root.right
#         else:
#             root.left=None
            
            
        """
        Do not return anything, modify root in-place instead.
        """
        