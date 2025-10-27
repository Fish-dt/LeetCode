class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        prev_count = 0
        total = 0

        for row in bank:
            cnt = row.count('1')
            if cnt:
                total += prev_count * cnt
                prev_count = cnt
        return total