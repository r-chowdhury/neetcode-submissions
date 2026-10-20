class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      ROWS, COLS = m, n
      directions = [
        [1,0], [0,1]
      ] 
      cache = {}

      def dfs(r, c):
        if r < 0 or c < 0 or r >= ROWS or c >= COLS:
          return 0

        if (r,c) == (ROWS - 1, COLS - 1):
           return 1
        
        if (r, c) in cache:
          return cache[(r, c)]

        res = 0
        for dr, dc in directions:
          res += dfs(r + dr, c + dc)
        
        cache[(r, c)] = res
        return res

      return dfs(0, 0)