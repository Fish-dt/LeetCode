class Solution(object):
    def minOperations(self, nums, k):
        total = sum(nums)
        r = total % k
        return r
        