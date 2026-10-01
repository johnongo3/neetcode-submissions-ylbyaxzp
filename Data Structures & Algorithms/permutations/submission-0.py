class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base: the length of the path is the same as the length of the nums array
        # constraint: the same number cant appear twice in the same path
        # choices: all numbers in nums
        # backtrack: pop the path to check the other numbers in nums

        def backtrack(path):
            # base case: we have our path of appropriate size
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                # constraint: the same number cant appear twice
                if num in path:
                    continue
                
                # backtracking step
                path.append(num)
                backtrack(path) # explore this path
                path.pop() # backtrack
        
        backtrack([])
        return res