class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> seen = new HashSet<>();
        int longestSeen = 0;

        int left = 0;
        int right = 0;
        while (right < s.length()) {
            if (!seen.contains(s.charAt(right))) {
                seen.add(s.charAt(right));
                right += 1;
                longestSeen = Math.max(longestSeen, right - left);
            } else {
                while (seen.contains(s.charAt(right))) {
                    seen.remove(s.charAt(left));
                    left++;
                }
            }
        }
        return longestSeen;
    }
}
