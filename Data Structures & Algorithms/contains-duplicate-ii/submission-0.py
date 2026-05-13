class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i, i + k + 1):
                if j < len(nums) and nums[i] == nums[j] and i != j:
                    return True

        return False