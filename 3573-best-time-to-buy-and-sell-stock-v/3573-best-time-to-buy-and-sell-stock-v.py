class Solution(object):
    def maximumProfit(self, prices, k):
        """
        :type prices: List[int]
        :type k: int
        :rtype: int
        """
        dp = [[-10**18, -10**18, -10**18] for _ in range(k + 1)]
        dp[0][0] = 0

        for p in prices:
            ndp = [row[:] for row in dp]
            for t in range(k + 1):
                ndp[t][1] = max(ndp[t][1], dp[t][0] - p)
                ndp[t][2] = max(ndp[t][2], dp[t][0] + p)
                if t < k:
                    ndp[t + 1][0] = max(ndp[t + 1][0], dp[t][1] + p)
                    ndp[t + 1][0] = max(ndp[t + 1][0], dp[t][2] - p)
            dp = ndp

        ans = 0
        for t in range(k + 1):
            ans = max(ans, dp[t][0])
        return ans