class Solution(object):
    def lengthOfLongestSubstring(self, s):
        subS=set()
        l=0
        res=0

        for r in range(len(s)):
            while s[r] in subS:
                subS.remove(s[l])
                l+=1
            subS.add(s[r])
            res=max(res,r-l+1)

        return res
        