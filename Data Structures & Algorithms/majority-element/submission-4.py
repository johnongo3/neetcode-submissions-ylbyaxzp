class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        char_freq = {}

        for num in nums:
            char_freq[num] = 1 + char_freq.get(num, 0)
        
        res = sorted(char_freq, key = lambda x: char_freq[x])

        return res[-1]