class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = prices[0];
        int biggestProfit = 0;
        for (int i = 0; i < prices.length; i++) {
            minPrice = Math.min(minPrice, prices[i]);
            biggestProfit = Math.max(biggestProfit, prices[i] - minPrice);
        }
        return biggestProfit;
    }
}
