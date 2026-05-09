class Solution:
    def trap(self, height: List[int]) -> int:
        # area of water captured = min(maxLeft, maxRight) - height[i]
        # pre-compute maxLeft and maxRight pointer arrays, i.e. max boundaries
        maxLeft = [0 * len(height)]
        max_seen_L = 0
        # maxLeft
        for i in range(1, len(height)):
            max_seen_L = max(max_seen_L, height[i - 1])
            maxLeft.append(max_seen_L)

        # maxRight
        maxRight = [0 * len(height)]
        max_seen_R = 0
        for i in range(len(height) - 2, -1, -1):
            max_seen_R = max(max_seen_R, height[i + 1])
            maxRight.append(max_seen_R)

        maxRight.reverse()
        totalWater = 0
        for i in range(len(height)):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            if water > 0:
                totalWater += water

        return totalWater
