class Solution(object):
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        a = b = -10**18
        res = 0
        
        for s, e in intervals:
            if s <= b:
                continue
            if s <= a:
                res += 1
                b = a
                a = e
            else:
                res += 2
                b = e - 1
                a = e
        
        return res