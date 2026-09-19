class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        original_s_letters = {}
        t_letters = {}

        for i in range(len(s)):
            if s[i] in original_s_letters:
                original_s_letters[s[i]] += 1
            else:
                original_s_letters[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in t_letters:
                t_letters[t[i]] += 1
            else:
                t_letters[t[i]] = 1
        
        for key, value in t_letters.items():
            if key not in original_s_letters:
                return key
                
            if original_s_letters[key] != value:
                return key
            