import heapq
from collections import Counter

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        if n == 0:
            return []

        freq = Counter()
        top_heap = []    
        rest_heap = []   
        in_top = set()
        sumTop = [0]     

        for i in range(min(k, n)):
            freq[nums[i]] += 1

        items = sorted(freq.items(), key=lambda t: (-t[1], -t[0]))
        for idx, (num, f) in enumerate(items):
            if idx < x:
                in_top.add(num)
                heapq.heappush(top_heap, (f, num))
                sumTop[0] += f * num
            else:
                heapq.heappush(rest_heap, (-f, -num))

        def pop_valid_top():
            while top_heap:
                f, nnum = top_heap[0]
                if freq.get(nnum, 0) != f or nnum not in in_top:
                    heapq.heappop(top_heap)
                    continue
                return f, nnum
            return None

        def pop_valid_rest():
            while rest_heap:
                nf, nn = rest_heap[0]
                f = -nf; nnum = -nn
                if freq.get(nnum, 0) != f or nnum in in_top:
                    heapq.heappop(rest_heap)
                    continue
                return f, nnum
            return None

        def ensure_balance():
            while len(in_top) < x:
                cand = pop_valid_rest()
                if not cand:
                    break
                f, nnum = cand
                heapq.heappop(rest_heap)
                in_top.add(nnum)
                heapq.heappush(top_heap, (f, nnum))
                sumTop[0] += f * nnum

            while True:
                worst = pop_valid_top()
                best = pop_valid_rest()
                if not worst or not best:
                    break
                f_w, n_w = worst
                f_b, n_b = best
                if (f_b > f_w) or (f_b == f_w and n_b > n_w):
                    heapq.heappop(top_heap)
                    heapq.heappop(rest_heap)
                    in_top.remove(n_w)
                    in_top.add(n_b)
                    sumTop[0] += f_b * n_b - f_w * n_w
                    heapq.heappush(top_heap, (f_b, n_b))
                    heapq.heappush(rest_heap, (-f_w, -n_w))
                else:
                    break

        res = [sumTop[0]]

        for i in range(k, n):
            out = nums[i - k]
            inn = nums[i]

            if freq.get(out, 0) > 0:
                if out in in_top:

                    sumTop[0] -= out
                if freq[out] == 1:
                    del freq[out]
                    if out in in_top:
                        in_top.remove(out)
                else:
                    freq[out] -= 1
                    if out in in_top:
                        heapq.heappush(top_heap, (freq[out], out))
                    else:
                        heapq.heappush(rest_heap, (-freq[out], -out))

            prev = freq.get(inn, 0)
            freq[inn] = prev + 1
            if inn in in_top:
                sumTop[0] += inn
                heapq.heappush(top_heap, (freq[inn], inn))
            else:
                heapq.heappush(rest_heap, (-freq[inn], -inn))

            ensure_balance()
            res.append(sumTop[0])

        return res
