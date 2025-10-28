class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        valid_count = 0

        def simulate(start, direction):
            arr = nums[:] 
            curr = start
            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += direction
                else:
                    arr[curr] -= 1
                    direction *= -1
                    curr += direction
            return all(x == 0 for x in arr)

        for i in range(n):
            if nums[i] == 0:
                if simulate(i, -1):
                    valid_count += 1
                if simulate(i, 1):
                    valid_count += 1

        return valid_count