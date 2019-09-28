#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
#
#The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
#
#Example:
#
#Input: [3,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6
#*/



class Solution:
    def trap(self, height: List[int]) -> int:
        right,left,water=len(height)-1,0,0
        
        while right >left:
            inc=1
            
            if (height[right]>height[left]):
                while height[left]>height[left+inc]:
                    water+=height[left]-height[left+inc]
                    inc+=1
                left+=inc
            else:
                while height[right]>height[right-inc]:
                    water+=height[right]-height[right-inc]
                    inc+=1
                right-=inc
            
                
        return water