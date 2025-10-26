"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldToNew={}
        def clone(node):
            if not node:
                return None
            if node in oldToNew:
                return oldToNew[node]
            copy=Node(node.val)
            oldToNew[node]=copy
            for nie in node.neighbors:
                copy.neighbors.append(clone(nie))
            return copy  
        return clone(node)      