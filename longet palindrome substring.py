Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"class Solution:
    def longestPalindrome(self, s: str) -> str:
        stack=[]
        if len(s)==1  :
            return s
        if   len(s)==0:
            return 0

        rstr=''
        result=[]
        
        for i in range(0,len(s)):
            for j in range(i+1,len(s)):
                temp=s[i:j+1]
                print((s[i:j]))
                if s[i:j+1]==temp[::-1]:
                    
                    #print(reversed(s[i:j]))
                    
                    return temp
            
            
        
        
        