class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        
        for a in range(1, n+1):
            for b in range(1, n+1):
                s = a*a + b*b
                c = int((s) ** 0.5)
                if c*c == s and c <= n:
                    count += 1
        
        return count
        