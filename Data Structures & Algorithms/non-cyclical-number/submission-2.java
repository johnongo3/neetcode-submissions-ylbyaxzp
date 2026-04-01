class Solution {
    public int getSum(int n) {
        int sum = 0;
        for (char ch : Integer.toString(n).toCharArray()) {
            sum += (ch - '0') * (ch - '0');
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
