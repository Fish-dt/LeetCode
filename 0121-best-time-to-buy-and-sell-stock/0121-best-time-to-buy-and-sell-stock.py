class Solution(object):
    def maxProfit(self, prices):
        l, r, biggest =0,1,0
        while r<len(prices):
            if prices[l]<prices[r]:
                biggest=max(biggest,prices[r]-prices[l])
            else:
                l=r
            r+=1
        return biggest
        