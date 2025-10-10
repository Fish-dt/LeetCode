class Solution(object):
    def topKFrequent(self, nums, k):
        freq=[]
        for n in nums:
            found=False
            for pairs in freq:
                if pairs[0]==n:
                    pairs[1]+=1
                    found=True
                    break
            if not found:
                freq.append([n,1])
        freq.sort(key=lambda x:x[1], reverse=True)
        result=[freq[f][0] for f in range(k)]

        return result
        