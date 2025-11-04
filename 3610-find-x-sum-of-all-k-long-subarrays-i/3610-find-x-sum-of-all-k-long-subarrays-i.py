from collections import Counter
class Solution(object):
    def findXSum(self, nums, k, x):
        n = len(nums)
        ans = []
        
        for i in range(n - k + 1):
            sub = nums[i:i + k]
            freq = Counter(sub)
            top = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            top_x = set([val for val, _ in top[:x]])
            s = sum(num for num in sub if num in top_x)
            ans.append(s)
        
        return ans
        