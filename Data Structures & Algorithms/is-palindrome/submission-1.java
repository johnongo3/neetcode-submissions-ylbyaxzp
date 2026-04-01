class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int startPtr = 0;
        int endPtr = s.length() - 1;

        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(startPtr) != s.charAt(endPtr)) {
                return false;
            }
            startPtr++;
            endPtr--;
        }
        return true;
    }
}
