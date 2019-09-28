Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left, pointer = 0, 0 
        
        while pointer < len(nums):
            if nums[pointer] == 0:
                pointer+=1 
                
            else:
                nums[pointer], nums[left] = nums[left], nums[pointer]
                print(nums[pointer],pointer, nums[left],left)
                pointer, left = pointer+1, left+1
