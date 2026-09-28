class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        unexp = 2147483647

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))

        while len(q) > 0:
            r, c = q.popleft()

            for path in directions:
                dr, dc = r + path[0], c + path[1]
                if (dr in range(len(grid)) and dc in range(len(grid[0])) and grid[dr][dc] != -1):
                    if grid[dr][dc] == 0:
                        continue
                    
                    if grid[dr][dc] == unexp:
                        q.append((dr, dc))
                        grid[dr][dc] = grid[r][c] + 1
                    else:
                        grid[dr][dc] = min(grid[r][c] + 1, grid[dr][dc])

