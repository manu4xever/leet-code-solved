Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans=[[]]
        for i in nums:
            for y in range(len(ans)):
                print("ans[y]",ans[y])
                print("[i]",[i])
                
                ans.append(ans[y]+[i])
                print("ans",ans)
        return ans