class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def bfs(r,c):
            q = deque()
            grid[r][c] = 0
            a = 1
            q.append((r,c))
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == 0):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    a += 1
            return a
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    a = bfs(r,c)
                    if a > maxArea:
                        maxArea = a
        return maxArea

