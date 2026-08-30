class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True
    
   

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.add_word(w)

        def dfs(r, c, node, seen = None, word = None):
            char = board[r][c]
            if char not in node.children:
                return

            node = node.children[char]
            seen.add((r,c))
            word.append(char)

            if node.is_word:
                res.append("".join(word))
                node.is_word = False

            dimensions = ((1,0), (0,1), (-1,0), (0,-1))
            for dr, dc in dimensions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nc >= 0 and nr < len(board) and nc < len(board[nr]) and (nr,nc) not in seen:
                    dfs(nr, nc, node, seen, word)

            seen.remove((r,c))
            word.pop()

        res = []
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] in root.children:
                    dfs(r, c, root, set(), [])
                            
        return res