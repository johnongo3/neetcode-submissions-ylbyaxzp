class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        j = len(arr) - 1
        curr_max = 0
        while j >= 0:
            if j == len(arr) - 1:
                curr_max = arr[j]
            else:
                res[j] = curr_max
                curr_max = max(curr_max, arr[j])
            j -= 1
        return res