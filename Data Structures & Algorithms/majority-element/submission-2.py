class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        char_freq = {}

        for num in nums:
            if num in char_freq and char_freq[num] >= len(nums) // 2:
                return num
            elif num in char_freq:
                char_freq[num] += 1
            else:
                char_freq[num] = 1
        
        return nums[0]
