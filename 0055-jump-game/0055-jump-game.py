class Solution(object):
    def canJump(self, nums):
        goal=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if goal<=nums[i]+i:
                goal=i
        return not goal
        