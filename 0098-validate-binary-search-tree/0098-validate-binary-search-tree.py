class Solution(object):
    def isValidBST(self, root):
        def checker(node, left, right):
            if not node:
                return True
            if not ((node.val>left)  and (node.val<right)):
                return False
            return (checker(node.left, left, node.val) and checker(node.right,node.val,right))
        return (checker(root, float("-inf"), float("inf")))
        