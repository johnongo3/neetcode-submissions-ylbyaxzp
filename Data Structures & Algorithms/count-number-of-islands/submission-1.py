class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # collect all the 1s into a queue
        # pop, bfs on a 1 grid, and add into a visited set.
        # keep dequing, if the grid we deque is in the visited set, we move on.
        # otherwise its a new island.
        n_rows, n_cols = len(grid), len(grid[0]) # assuming rectangular matrix

        island_q = collections.deque()
        explore_q = collections.deque()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island_q.append((i, j))
        
        if len(island_q) == 0:
            return 0

        # we need a source, so have first entry in island_q as our start
        entry = island_q.popleft()
        visited.add(entry)
        explore_q.append(entry)
        islands = 1
        
        while len(island_q) > 0:
            r, c = explore_q.popleft()
            for path in directions:
                new_r, new_c = r + path[0], c + path[1]
                in_bounds = 0 <= new_r < n_rows and 0 <= new_c < n_cols
                if (in_bounds and grid[new_r][new_c] == "1"):
                    if (new_r, new_c) not in visited:
                        explore_q.append((new_r, new_c))
                        visited.add((new_r, new_c))

            # iterate through island_q until we get a non-explored island
            if len(explore_q) == 0:
                while True:
                    if len(island_q) == 0:
                        break

                    r, c = island_q.popleft()
                    if (r, c) in visited:
                        continue
                    else:
                        explore_q.append((r, c))
                        islands += 1
                        break
                                          

        return islands