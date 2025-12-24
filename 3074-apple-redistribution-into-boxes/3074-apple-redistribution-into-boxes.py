class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total_apples = sum(apple)
        capacity.sort(reverse=True)

        curr = 0
        boxes = 0

        for c in capacity:
            curr += c
            boxes += 1
            if curr >= total_apples:
                return boxes
        