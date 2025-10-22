class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        cnt = Counter(nums)
        diff = defaultdict(int)
        for num in nums:
            diff[num - k] += 1
            diff[num + k + 1] -= 1
        for num in nums:
            if num not in diff:
                diff[num] += 0

        ans = 1
        s = 0
        for x in sorted(diff.keys()):
            s += diff[x]
            cnt_x = cnt.get(x, 0)
            ans = max(ans, cnt_x + min(numOperations, s - cnt_x))
        return ans
        