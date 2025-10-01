class Solution(object):
    def containsDuplicate(self, nums):
        nums = sorted(nums)
        array_length = len(nums)
        for i in range(1, array_length):
            prev = i - 1
            if nums[i] == nums[prev]:
                return True
        return False
