Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        #print(nums)
       
        for i in range (0,len(nums)-2):
                 left=i+1
                 right=len(nums)-1
                
                 while right>left:
                    #print(nums[i],nums[right],nums[left])
                    if nums[i]+nums[right]+nums[left]<0:
                        left+=1
                    elif nums[i]+nums[right]+nums[left]>0:
                         right-=1
                    elif nums[i]+nums[right]+nums[left]==0:
                        res.add((nums[i],nums[right],nums[left]))
                        right-=1
                        left+=1
        return list(res)
        