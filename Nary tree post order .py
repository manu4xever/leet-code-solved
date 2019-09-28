"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        if not root.children:
            return [root.val]
        res=[]
        for child in root.children:
            c= self.postorder(child)
            res.extend(c)
        
        return res+[root.val]