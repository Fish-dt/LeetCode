class Solution(object):
    def maxOperations(self, s):
        ones = 0
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):
            if ch == '1':
                ones += 1
            else:
                if i + 1 == n or s[i + 1] == '1':
                    ans += ones
        return ans

