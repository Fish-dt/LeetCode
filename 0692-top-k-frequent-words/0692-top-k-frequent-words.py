class Solution(object):
    def topKFrequent(self, words, k):
        freq=[]
        for n in words:
            found=False
            for pair in freq:
                if pair[0]==n:
                    pair[1]+=1
                    found=True
            if not found:
                freq.append([n,1])
        freq.sort(key=lambda x: (-x[1],x[0]))
        result=[freq[i][0] for i in range(min(k,len(freq)))]
        return result