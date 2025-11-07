class Solution:
    def maxPower(self, stations, r, k):
        n = len(stations)
        
        power = [0] * n
        window_sum = 0
        left = 0
        for i in range(n):
            while i - left > r:
                window_sum -= stations[left]
                left += 1
            if i + r < n:
                window_sum += stations[i + r]
            power[i] = window_sum
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stations[i]
        for i in range(n):
            left = max(0, i - r)
            right = min(n, i + r + 1)
            power[i] = prefix[right] - prefix[left]

        def canReach(x):
            added = [0] * (n + 1) 
            curr_add = 0
            remain = k
            for i in range(n):
                curr_add += added[i]
                if power[i] + curr_add < x:
                    need = x - (power[i] + curr_add)
                    if need > remain:
                        return False
                    remain -= need
                    curr_add += need
                    end = min(n, i + 2 * r + 1)
                    added[end] -= need
            return True
        
        lo, hi = 0, sum(stations) + k
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if canReach(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
