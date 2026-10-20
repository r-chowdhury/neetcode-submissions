class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        res = [False]
        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        def dfs(r, c, i, running_str):
            if i == len(word):
                if running_str == word:
                    res[0] = True
                return
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited
            or board[r][c] != word[i]):
                return
            if word[i] == board[r][c]:
                running_str += board[r][c]
            visited.add((r, c)) 
            for dr, dc in directions:
                dfs(r + dr, c + dc, i + 1, running_str)
                if res[0]:
                    return
            visited.remove((r,c))
            return

        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, 0, "")
        return res[0]
            