class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            carIndex = abs(nums[i]) - 1
            if nums[carIndex] < 0:
                return abs(nums[i])
            else:
                nums[carIndex] *= -1
        return -1