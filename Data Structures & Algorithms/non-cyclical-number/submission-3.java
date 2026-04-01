class Solution {
    public int getSum(int n) {
        int sum = 0;
        while (n != 0) {
            sum += (int) Math.pow(n % 10, 2);
            n /= 10;
        }
        return sum;
    }

    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<>();
        int sumOfDigits = getSum(n);
        while (!seen.contains(sumOfDigits)) {
            if (sumOfDigits == 1) {
                return true;
            } else {
                seen.add(sumOfDigits);
                sumOfDigits = getSum(sumOfDigits);
            }
        }
        return false;
    }
}
