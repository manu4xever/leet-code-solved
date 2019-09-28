Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        count = 0
        def ret(root, count):
            if not root:#if there is no root
                return count
            count += 1
            countLeft = ret(root.left, count)
            countRight = ret(root.right, count)
            print(countRight, countLeft)
            if countLeft > countRight:
                return countLeft
            else:
                return countRight
        
            print(countRight, countLeft)
        return ret(root, count)