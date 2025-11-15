class Solution(object):
    def numberOfSubstrings(self, s):
        n = len(s)
        zeros = [-1]
        for i, c in enumerate(s):
            if c == '0':
                zeros.append(i)
        zeros.append(n)
        ans = 0
        last = -1
        for i, c in enumerate(s):
            if c == '0':
                L = i - last - 1
                ans += L * (L + 1) // 2
                last = i
        L = n - last - 1
        ans += L * (L + 1) // 2
        import math
        LIMIT = int(math.sqrt(n)) + 2
        zcount = len(zeros) - 2
        for z in range(1, LIMIT):
            if z > zcount:
                break
            z2 = z * z
            for i in range(1, zcount - z + 2):
                left_zero = zeros[i]
                right_zero = zeros[i + z - 1]
                L = left_zero - zeros[i - 1]
                R = zeros[i + z] - right_zero
                base_ones = (right_zero - left_zero + 1) - z
                need = z2 - base_ones
                total_pairs = L * R
                if need <= 0:
                    ans += total_pairs
                    continue
                max_sum = (L - 1) + (R - 1)
                if need > max_sum + 1:
                    continue
                t = need - 1
                max_a = min(L - 1, t)
                if max_a < 0:
                    pairs_le = 0
                else:
                    max_a_full = t - (R - 1)
                    if max_a_full < 0:
                        cnt_full = 0
                    else:
                        cnt_full = min(max_a_full, max_a) + 1
                    if max_a < cnt_full:
                        partial_terms = 0
                        partial_sum_a = 0
                    else:
                        partial_terms = max_a - cnt_full + 1
                        if partial_terms > 0:
                            a1 = cnt_full
                            a2 = max_a
                            partial_sum_a = (a1 + a2) * partial_terms // 2
                        else:
                            partial_sum_a = 0
                    pairs_le = cnt_full * R
                    pairs_le += partial_terms * (t + 1) - partial_sum_a
                ans += total_pairs - pairs_le
        return ans
