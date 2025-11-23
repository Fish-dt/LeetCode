class Solution(object):
    def maxSubArray(self, nums):
        maxSum=nums[0]
        curSum=0
        for n in nums:
            if curSum<0:
                curSum=0
            curSum+=n
            maxSum=max(maxSum, curSum)
        return maxSum
        