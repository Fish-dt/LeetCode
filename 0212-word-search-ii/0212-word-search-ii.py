class TrieNode:
    def __init__(self):
        self.children={}
        self.isWord=False

    def addWord(self, word):
        cur=self
        for w in word:
            if w not in cur.children:
                cur.children[w]=TrieNode()
            cur=cur.children[w]
        cur.isWord=True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root=TrieNode()
        for w in words:
            root.addWord(w)
        row, col = len(board), len(board[0])
        visit, res = set(), set()

        def dfs(r, c, node, word):     
            if (r<0 or c<0 or r==row or c==col or 
                board[r][c] not in node.children or (r, c) in visit):
                return
            visit.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)
            visit.remove((r,c))
        for r in range(row):
            for c in range(col):
                dfs(r,c,root,"")
        return list(res)