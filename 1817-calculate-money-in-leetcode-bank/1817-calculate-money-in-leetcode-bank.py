class Solution(object):
    def totalMoney(self, n):
        total = 0
        week_start = 1 
        day = 0

        while n > 0:
            for i in range(7):
                if n == 0:
                    break
                total += week_start + i
                n -= 1
            week_start += 1
        return total