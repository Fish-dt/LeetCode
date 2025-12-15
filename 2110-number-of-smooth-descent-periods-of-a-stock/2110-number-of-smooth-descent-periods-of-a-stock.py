class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 1
        length = 1

        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                length += 1
            else:
                length = 1
            ans += length

        return ans
        