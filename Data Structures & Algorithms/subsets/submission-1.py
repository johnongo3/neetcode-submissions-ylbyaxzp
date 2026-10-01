class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # base case
        # constraints: no constraints
        # choice: numbers which are unique
        # backtrack
        res = []

        def backtrack(index, subset):
            # base case: length of the subset is equal to length of nums
            if index == len(nums):
                res.append(subset[:])
                return
            
            # decision 1: include nums[index]
            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()

            # decision 2: dont include nums[index]
            backtrack(index + 1, subset)
            
        backtrack(0, [])
        return res