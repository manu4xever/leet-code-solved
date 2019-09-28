Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:return []
        if len(nums)==1 :return nums
        if len(nums)==2 :return reversed(nums)
        res1=[1]*(len(nums))
        res2=[1]*(len(nums))
        for i in range(1,len(nums)):
            #print(i,j,k)
            res1[i]*=res1[i-1]*nums[i-1]
            
        #print(res1)
        
        for i in range(len(nums)-2,-1,-1):
            
            res2[i]*=res2[i+1]*nums[i+1]
            #print(res2[i],"nums", res2[i+],res2[])
            # j-=1
            # k-=1
        # print(res2)
        # print(type(res2),type(res1))
        # [a*b for a,b in zip(res1,res2)]
        # res1*=res2

        return [a*b for a,b in zip(res1,res2)]
        