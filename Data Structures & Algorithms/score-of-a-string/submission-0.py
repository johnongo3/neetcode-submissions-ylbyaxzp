class Solution:
    def scoreOfString(self, s: str) -> int:
        l, r = 0, 1
        res = 0
        while r < len(s):
            res += abs(ord(s[r]) - ord(s[l]))
            l += 1
            r += 1
        return res