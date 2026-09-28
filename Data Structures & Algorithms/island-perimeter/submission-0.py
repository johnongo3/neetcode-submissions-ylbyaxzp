class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        visited = set()

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    q.append((r, c))
                    visited.add((r, c))
                    break
        
            if len(q) != 0:
                break
        
        perimeter = 0
        i = 0
        while len(q) > 0:
            r, c = q.popleft()
            for path in directions:
                dr, dc = r + path[0], c + path[1]
                if (dr in range(len(grid)) and dc in range(len(grid[0]))):
                    if grid[dr][dc] == 1:
                        if (dr, dc) not in visited:
                            q.append((dr, dc))
                            visited.add((dr, dc))
                    else:
                        perimeter += 1
                else:
                    perimeter += 1
            
        return perimeter