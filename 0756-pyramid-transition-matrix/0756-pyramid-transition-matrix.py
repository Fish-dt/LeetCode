class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        from collections import defaultdict
        memo = {}

        mp = defaultdict(list)
        for a in allowed:
            mp[a[:2]].append(a[2])

        def dfs(row):
            if len(row) == 1:
                return True
            if row in memo:
                return memo[row]

            def build(i, next_row):
                if i == len(row) - 1:
                    return dfs(next_row)

                pair = row[i:i+2]
                if pair not in mp:
                    return False

                for ch in mp[pair]:
                    if build(i + 1, next_row + ch):
                        return True
                return False

            memo[row] = build(0, "")
            return memo[row]

        return dfs(bottom)
        