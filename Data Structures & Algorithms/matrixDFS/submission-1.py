class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
      ROWS = len(grid)
      COLS = len(grid[0])
      visited = set()
      directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1)
      ]

      def dfs(r, c, visited):
        if r == ROWS or c == COLS or r < 0 or c < 0 or (r,c) in visited or grid[r][c] == 1:
          return 0
        if r == ROWS - 1 and c == COLS - 1:
          return 1
        visited.add((r,c))
        count = 0
        for dr, dc in directions:
          count += dfs(r + dr, c + dc, visited)
        
        visited.remove((r,c))
        return count

      return dfs(0, 0, visited)