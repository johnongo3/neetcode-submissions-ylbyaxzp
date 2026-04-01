class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();

        // send heaviest stones to the front
        for (int stone : stones) {
            maxHeap.add(-stone);
        }

        // continually smash the stones together
        while (maxHeap.size() > 1) {
            int stone1 = maxHeap.poll();
            int stone2 = maxHeap.poll();

            if (stone1 == stone2) {
                continue;
            } else if (stone1 > stone2) {
                stone2 = stone2 - stone1;
                maxHeap.add(stone2);
            } else {
                stone1 = stone1 - stone2;
                maxHeap.add(stone1);
            }
        }

        return maxHeap.isEmpty() ? 0 : Math.abs(maxHeap.peek());
    }
}
