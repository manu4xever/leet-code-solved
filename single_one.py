Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
class Solution {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        int size = nums.length;
        int index1=0;
        int index2=1;
        if (size==1){
            return nums[0];
        }
        while (index1<size-1){
            if (nums[index1]!= nums[index2]){break; }
            index1+=2;
            index2+=2;
        }
        return nums[index1];
    }
}