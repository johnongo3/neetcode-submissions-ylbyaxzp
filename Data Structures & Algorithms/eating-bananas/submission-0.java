class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        Arrays.sort(piles);
        int l = 1;
        int r = piles[piles.length - 1];
        int result = r;

        while (l <= r) {
            int mid = (l + r) / 2;
            long totalTime = 0;
            for (int p : piles) {
                totalTime += Math.ceil((double) p / mid);
            }

            if (totalTime <= h) {
                result = mid;
                r = mid - 1;    
            } else {
                l = mid + 1;
            }
        }
        return result;
    }
}
