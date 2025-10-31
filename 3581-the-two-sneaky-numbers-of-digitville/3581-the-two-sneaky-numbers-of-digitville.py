class Solution(object):
    def getSneakyNumbers(self, nums):
        count=Counter(nums)
        return [num for num, freq in count.items() if freq==2]
        