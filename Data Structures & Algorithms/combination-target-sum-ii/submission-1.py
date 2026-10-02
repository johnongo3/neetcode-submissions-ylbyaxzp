class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # base case: sum = target
        # constraints: integers need to be used once, but can be returned in any order, and combination can be in any order
        # choices: each number from candidates
        res = []
        candidates.sort()

        def backtrack(idx, total, path):
            # Base cases
            if total == target:
                res.append(path[:])  
                return
            if total > target:
                return

            # choices
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, total + candidates[i], path)
                path.pop()

        backtrack(0, 0, [])
        return res