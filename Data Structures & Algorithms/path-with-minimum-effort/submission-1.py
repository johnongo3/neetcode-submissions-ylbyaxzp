class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        # Priority Queue stores: (effort_so_far, row, col)
        frontier = [(0, 0, 0)]
        visited = set()

        while frontier:
            diff, r, c = heapq.heappop(frontier)
            
            if (r, c) in visited:
                continue
            visited.add((r, c))

            # Reached destination
            if r == rows - 1 and c == cols - 1:
                return diff
            
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_r, new_c = r + dr, c + dc
                
                if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited:
                    new_diff = max(diff, abs(heights[r][c] - heights[new_r][new_c]))
                    heapq.heappush(frontier, (new_diff, new_r, new_c))
        
        return 0