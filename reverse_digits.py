Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=[]
        
        for i in str(x)[::-1]:
            a.append(i)
        #print ("".join(a))
        
        
        if x<0:
            i=int(("".join(a[:len(a)-1])))
            return -i if -2147483648 <= i <= 2147483647 else 0
        else:return int(("".join(a))) if -2147483648 <= int(("".join(a))) <= 2147483647 else 0