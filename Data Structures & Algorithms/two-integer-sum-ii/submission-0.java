class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // 2 ptr bin search
        int lowPtr = 0;
        int hiPtr = numbers.length - 1;

        while (lowPtr < hiPtr) {
            int sum = numbers[lowPtr] + numbers[hiPtr];
            if (sum == target) {
                return new int[] {lowPtr + 1, hiPtr + 1};
            }

            if (sum < target) {
                lowPtr++;
            } else if (sum > target) {
                hiPtr--;
            }
        }
        return null;
    }
}
