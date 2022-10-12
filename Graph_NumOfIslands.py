from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return None

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(i, j):
            q = deque()
            visited.add((i, j))
            q.append((i, j))
    
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for r, c in directions:
                    i, j = row+r, col+c
                    if (i in range(rows) and
                        j in range(cols) and
                        grid[i][j] == "1" and
                        (i, j) not in visited):
                        q.append((i, j))
                        visited.add((i, j))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands
