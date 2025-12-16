class Solution(object):
    def maxProfit(self, n, present, future, hierarchy, budget):
        """
        :type n: int
        :type present: List[int]
        :type future: List[int]
        :type hierarchy: List[List[int]]
        :type budget: int
        :rtype: int
        """
        tree = [[] for _ in range(n)]
        for u, v in hierarchy:
            tree[u - 1].append(v - 1)

        def merge(a, b):
            res = [-10**18] * (budget + 1)
            for i in range(budget + 1):
                if a[i] < 0:
                    continue
                for j in range(budget - i + 1):
                    res[i + j] = max(res[i + j], a[i] + b[j])
            return res

        def dfs(u):
            dp_no = [0] * (budget + 1)
            dp_yes = [0] * (budget + 1)

            for v in tree[u]:
                c_no, c_yes = dfs(v)
                dp_no = merge(dp_no, c_no)
                dp_yes = merge(dp_yes, c_yes)

            full_cost = present[u]
            half_cost = present[u] // 2
            full_profit = future[u] - full_cost
            half_profit = future[u] - half_cost

            new_no = dp_no[:]
            new_yes = dp_no[:]

            for b in range(full_cost, budget + 1):
                new_no[b] = max(new_no[b], dp_yes[b - full_cost] + full_profit)

            for b in range(half_cost, budget + 1):
                new_yes[b] = max(new_yes[b], dp_yes[b - half_cost] + half_profit)

            return new_no, new_yes

        return max(dfs(0)[0])