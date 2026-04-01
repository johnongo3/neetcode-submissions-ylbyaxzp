class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sDecomp = decomposeString(s);
        HashMap<Character, Integer> tDecomp = decomposeString(t);

        for (char c : sDecomp.keySet()) {
            if (!tDecomp.remove(c, sDecomp.get(c))) {
                return false;
            }
        }
        if (tDecomp.size() != 0) {
            return false;
        }

        return true;
    }

    public HashMap decomposeString(String x) {
        HashMap<Character, Integer> charCount = new HashMap<>();
        for (char c : x.toCharArray()) {
            if (charCount.get(c) != null) {
                charCount.put(c, charCount.get(c) + 1);
            } else {
                charCount.put(c, 1);
            }
        }
        return charCount;
    }
}
