class Solution(object):
    def maxSumDivThree(self, nums):
        total = sum(nums)

        r1 = []
        r2 = []

        for x in nums:
            if x % 3 == 1:
                r1.append(x)
            elif x % 3 == 2:
                r2.append(x)

        r1.sort()
        r2.sort()

        if total % 3 == 0:
            return total

        if total % 3 == 1:
            remove1 = r1[0] if r1 else float('inf')
            remove2 = sum(r2[:2]) if len(r2) >= 2 else float('inf')
            return total - min(remove1, remove2)

        if total % 3 == 2:
            remove1 = r2[0] if r2 else float('inf')
            remove2 = sum(r1[:2]) if len(r1) >= 2 else float('inf')
            return total - min(remove1, remove2)
        