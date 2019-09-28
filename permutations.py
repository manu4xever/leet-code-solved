Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(combination, digits):
            if not digits:
                ans.append(combination)
            else:
                for idx, num in enumerate(digits):
                    print(combination + [num],"num",[num],"combi",combination)
                    print(digits[:idx],"dig[:idx]",digits[idx+1:],"digs[idx+1:]")
                    backtrack(combination + [num], digits[:idx] + digits[idx+1:])
                
        ans = []
        backtrack([], nums)
        return ans