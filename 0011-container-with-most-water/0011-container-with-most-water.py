class Solution(object):
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        highest = 0
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            highest = max(highest, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return highest
