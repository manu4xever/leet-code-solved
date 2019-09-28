Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = []
        for i in strs:
            m =''.join (sorted(i))
            a.append(m)
        print(a)
        d={}
        for i in range(0,len(a)):
            if a[i] not in d:
                d[a[i]]=[strs[i]]
            else:
                #print(type(d[a[i]]))
                d[a[i]].append(strs[i])
        res = []
        for i in d:
            res.append(d[i])
        return res