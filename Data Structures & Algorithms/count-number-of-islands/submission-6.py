from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    grid[r][c] = "0"
                    q = deque([(r, c)])
                    while q:
                        cr, cc = q.popleft()
                        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                q.append((nr, nc))
        return islands