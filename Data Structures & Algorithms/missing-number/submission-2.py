class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for r in range(len(nums) + 1):
            if r not in nums:
                return r