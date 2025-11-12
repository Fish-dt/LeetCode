class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def minOperations(self, nums):
        n = len(nums)
        overall_gcd = nums[0]
        for num in nums[1:]:
            overall_gcd = self.gcd(overall_gcd, num)
        if overall_gcd != 1:
            return -1
        
        if 1 in nums:
            return n - nums.count(1)
        
        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = self.gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        
        return (min_len - 1) + (n - 1)
