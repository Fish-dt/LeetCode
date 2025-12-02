class Solution(object):
    def countTrapezoids(self, points):
        MOD = 10**9 + 7
        from collections import Counter

        freq = Counter(y for _, y in points)

        h_values = []
        for c in freq.values():
            if c >= 2:
                h = c * (c - 1) // 2
                h_values.append(h)

        if len(h_values) < 2:
            return 0

        sum_h = 0
        sum_h2 = 0

        for h in h_values:
            sum_h = (sum_h + h) % MOD
            sum_h2 = (sum_h2 + h * h) % MOD

        ans = (sum_h * sum_h - sum_h2) % MOD
        ans = ans * pow(2, MOD - 2, MOD) % MOD
        return ans
        