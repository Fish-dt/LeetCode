class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot: return True
        if not root: return False
        if self.sameTree(root,subRoot):
            return True
        return ((self.isSubtree(root.left,subRoot)or(self.isSubtree(root.right,subRoot))))
    def sameTree(self, r, t):
        if not r and not t:
            return True
        if r and t and r.val==t.val:
            return((self.sameTree(r.left,t.left) and (self.sameTree(r.right,t.right))))
        return False