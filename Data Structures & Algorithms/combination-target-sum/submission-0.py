class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # base case: sum of list = target
        # constraint: sum has to be less than or equal to target.
        # choices: all numbers from nums
        res = []
        nums.sort()

        def backtrack(idx, path, total):
            if total == target:
                res.append(path[:])
                return

            for j in range(idx, len(nums)):
                if total + nums[j] > target:
                    return
                path.append(nums[j])
                backtrack(j, path, total + nums[j])
                path.pop()

        backtrack(0, [], 0)
        return res