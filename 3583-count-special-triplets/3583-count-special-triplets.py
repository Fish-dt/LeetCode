class Solution(object):
    def specialTriplets(self, nums):
        MOD = 10**9 + 7

        from collections import Counter
        right = Counter(nums)
        left = Counter()

        ans = 0

        for j in range(len(nums)):
            val = nums[j]
            right[val] -= 1 

            need = val * 2

            leftCount = left[need]
            rightCount = right[need]

            ans = (ans + leftCount * rightCount) % MOD

            left[val] += 1 

        return ans
        