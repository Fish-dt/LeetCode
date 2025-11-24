class Solution(object):
    def prefixesDivBy5(self, nums):
        ans = []
        curr = 0

        for b in nums:
            curr = (curr * 2 + b) % 5
            ans.append(curr == 0)

        return ans
        