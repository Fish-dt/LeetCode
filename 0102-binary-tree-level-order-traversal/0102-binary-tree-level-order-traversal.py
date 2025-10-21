class Solution(object):
    def levelOrder(self, root):
        res=[]
        q = collections.deque()
        q.append(root)
        while q:
            level=[]
            qLen=len(q)
            for i in range(qLen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
