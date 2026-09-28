class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        frontier = collections.deque()
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        frontier.append((sr, sc))

        while len(frontier) > 0:
            r, c = frontier.popleft()
            for path in directions:
                dr, dc = r + path[0], c + path[1]
                in_bounds = dr in range(len(image)) and dc in range(len(image[0]))
                if in_bounds and image[dr][dc] == image[r][c]:
                    if (dr, dc) not in visited:
                        frontier.append((dr, dc))
                        visited.add((dr, dc))
            
            image[r][c] = color
        return image