class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = {}
        last = {}

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        ans = 0
        
        for ch in first:
            l = first[ch]
            r = last[ch]
            if r - l < 2:
                continue  

            middle_chars = set(s[l+1:r])
            ans += len(middle_chars)

        return ans