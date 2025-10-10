class Solution(object):
    def isPalindrome(self, s):
        newStr=[]
        for a in s:
            if a.isalnum():
                newStr+=lower(a)
        if newStr==newStr[::-1]:
            return True
        return False
        