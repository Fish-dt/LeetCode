class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        events.sort(key=lambda x: (int(x[1]), -(x[0] == "OFFLINE")))
        ans = [0] * numberOfUsers
        online_until = [0] * numberOfUsers
        
        for typ, ts, s in events:
            t = int(ts)
            
            if typ == "OFFLINE":
                uid = int(s)
                online_until[uid] = t + 60
            else:
                if s == "ALL":
                    for i in range(numberOfUsers):
                        ans[i] += 1
                elif s == "HERE":
                    for i in range(numberOfUsers):
                        if t >= online_until[i]:
                            ans[i] += 1
                else:
                    for token in s.split():
                        uid = int(token[2:])
                        ans[uid] += 1
        return ans