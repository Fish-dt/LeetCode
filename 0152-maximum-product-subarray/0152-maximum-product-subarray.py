class Solution(object):
    def maxProduct(self, nums):
        res=max(nums)
        curMax, curMin=1,1

        for n in nums:
            if n==0:
                curMax, curMin=1,1
                continue
            temp=curMax*n
            curMax=max(curMax*n, curMin*n, n)
            curMin=min(temp,curMin*n,n)
            res=max(curMax, res)
        return res