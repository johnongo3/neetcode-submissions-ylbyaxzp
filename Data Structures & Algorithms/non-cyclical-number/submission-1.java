class Solution {
    public int getSum(int n) {
        int sum = 0;
        char[] separated = Integer.toString(n).toCharArray();
        for (char ch : separated) {
            sum += (Character.getNumericValue(ch) * Character.getNumericValue(ch));
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
