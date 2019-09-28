Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        path=""
        
        self.dfs(0,0,n,path,res)
        return res
    def dfs(self, leftRemain, rightRemain,n, path, res):
        if (len(path)==2*n):
            res.append(path)
            return 
        if(leftRemain<n):
            self.dfs(leftRemain+1, rightRemain,n, path+'(',res)
            #print(path)
        if(leftRemain>rightRemain):
            self.dfs(leftRemain, rightRemain+1,n,path+')',res)
            #print(path)
        