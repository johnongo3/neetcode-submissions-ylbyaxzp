class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numIndex = new HashMap();

        for (int i = 0; i < nums.length; i++) {
            if (numIndex.keySet().contains(target - nums[i])) {
                int[] arr = {numIndex.get(target - nums[i]), i};
                return arr;
            }
            numIndex.put(nums[i], i);
        }
        return null;
    }
}
