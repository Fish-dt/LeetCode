class Solution(object):
    def maxProfit(self, prices, strategy, k):
        """
        :type prices: List[int]
        :type strategy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prices)

        base_profit = 0
        for i in range(n):
            base_profit += strategy[i] * prices[i]

        pref_sp = [0] * (n + 1)
        pref_p = [0] * (n + 1)

        for i in range(n):
            pref_sp[i + 1] = pref_sp[i] + strategy[i] * prices[i]
            pref_p[i + 1] = pref_p[i] + prices[i]

        best = base_profit
        half = k // 2

        for l in range(n - k + 1):
            mid = l + half
            r = l + k

            remove = pref_sp[mid] - pref_sp[l]
            add = (pref_p[r] - pref_p[mid]) - (pref_sp[r] - pref_sp[mid])

            curr = base_profit - remove + add
            if curr > best:
                best = curr

        return best

        