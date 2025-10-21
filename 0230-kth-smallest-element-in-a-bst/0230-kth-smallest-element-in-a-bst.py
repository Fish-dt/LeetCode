class Solution(object):
    def kthSmallest(self, root, k):
        n=0
        stack=[]
        pos=root

        while pos or stack:
            while pos:
                stack.append(pos)
                pos=pos.left
            
            pos=stack.pop()
            n+=1
            if n==k:
                return pos.val
            pos=pos.right

