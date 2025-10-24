class Solution(object):
    def nextBeautifulNumber(self, n):
        def isBalanced(x):
            cnt = [0] * 10
            y = x
            while y > 0:
                d = y % 10
                if d == 0:
                    return False
                cnt[d] += 1
                y //= 10
            for d in range(1, 10):
                if cnt[d] != 0 and cnt[d] != d:
                    return False
            return True
        
        candidate = n + 1
        while True:
            if isBalanced(candidate):
                return candidate
            candidate += 1
        