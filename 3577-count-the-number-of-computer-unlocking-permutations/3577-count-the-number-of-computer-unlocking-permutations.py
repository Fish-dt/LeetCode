class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(complexity)

        pref = complexity[0]
        for i in range(1, n):
            if pref >= complexity[i]:
                return 0
            if complexity[i] < pref:
                pref = complexity[i]

        ans = 1
        for k in range(1, n):
            ans = ans * k % MOD
        return ans