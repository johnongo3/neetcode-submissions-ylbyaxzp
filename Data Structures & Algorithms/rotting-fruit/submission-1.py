class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        rows, colms = len(grid), len(grid[0])

        q = collections.deque()
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

        for r in range(rows):
            for c in range(colms):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for row, col in directions:
                    nr = r + row
                    nc = c + col
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= colms or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1