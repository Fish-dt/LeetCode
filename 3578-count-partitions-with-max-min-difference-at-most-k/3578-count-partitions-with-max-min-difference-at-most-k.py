class Solution(object):
    def countPartitions(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)

        dp = [0] * (n + 1)
        pref = [0] * (n + 1) 

        dp[0] = 1
        pref[0] = 1

        from collections import deque
        
        maxdq = deque()
        mindq = deque()

        l = 0

        for r in range(n):
            while maxdq and maxdq[-1] < nums[r]:
                maxdq.pop()
            maxdq.append(nums[r])

            while mindq and mindq[-1] > nums[r]:
                mindq.pop()
            mindq.append(nums[r])

            while maxdq[0] - mindq[0] > k:
                if maxdq[0] == nums[l]:
                    maxdq.popleft()
                if mindq[0] == nums[l]:
                    mindq.popleft()
                l += 1

            dp[r+1] = (pref[r] - (pref[l-1] if l > 0 else 0)) % MOD

            pref[r+1] = (pref[r] + dp[r+1]) % MOD

        return dp[n] % MOD
        