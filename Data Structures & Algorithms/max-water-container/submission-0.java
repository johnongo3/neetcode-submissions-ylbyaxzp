class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int maxArea = 0;

        while (left < right) {
            int area = (right - left) * Math.min(heights[left], heights[right]);
            maxArea = Math.max(area, maxArea);

            // increment / decrement the smaller container wall
            if ((heights[right] == heights[left] && heights[right] == heights.length - 1) || heights[right] < heights[left]) {
                right--;
            } else {
                left++;
            }
        }
        return maxArea;
    }
}
