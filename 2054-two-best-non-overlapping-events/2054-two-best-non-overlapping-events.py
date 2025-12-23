class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        import heapq
        heap = []
        best = 0
        ans = 0

        for s, e, v in events:
            while heap and heap[0][0] < s:
                best = max(best, heapq.heappop(heap)[1])
            ans = max(ans, best + v)
            heapq.heappush(heap, (e, v))

        return ans