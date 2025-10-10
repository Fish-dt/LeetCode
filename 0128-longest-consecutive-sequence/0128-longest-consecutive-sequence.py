class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        nums=sorted(set(nums))

        longest, count=1,1
        for i in range(1,len(nums)):
            if 1+nums[i-1]==nums[i]:
                count+=1
            else:
                count=1
            if count>longest:
                longest=count
        return longest
            


        