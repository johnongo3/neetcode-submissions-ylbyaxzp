class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def getCharFreq(st: str) -> dict:
            char_freq = {}
            
            for char in st:
                if char not in char_freq:
                    char_freq[char] = 1
                else:
                    char_freq[char] += 1

            return char_freq

        s_char_freq = getCharFreq(s)
        t_char_freq = getCharFreq(t)

        for k in t_char_freq.keys():
            if k not in s_char_freq or s_char_freq[k] != t_char_freq[k]:
                return k

        return None
        