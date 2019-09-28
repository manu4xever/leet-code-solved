Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        #return root.val
        if not root:
            return []
        if not root.right and not root.left:
            return root
        queue =[root]
        
        
        visit=[root.val]
        while queue :
            right=[]
            for elem in  queue:
                
                
                if elem.left:
                    right.append(elem.left)
                if elem.right:                    
                    right.append(elem.right)
            
            if right:
                queue= right[-1]
                #print(type(queue))
                #return queue.val
                x=queue.val
                visit.append(x)
                #return visit
            queue= right
                
                        
                          
            
        return visit