class Solution:
    def merge(self, nums: List[int], l: int, m: int, r: int) -> None:
        n1 = m - l + 1 # size of first half
        n2 = r - m # size of second half
        L, R = nums[l:m + 1], nums[m + 1:r + 1]
        i, j, k = 0, 0, l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                nums[k] = L[i]
                k, i = k + 1, i + 1
            else:
                nums[k] = R[j]
                k, j = k + 1, j + 1
        
        while i < n1: # copy rest of L into nums
            nums[k] = L[i]
            k, i = k + 1, i + 1
        while j < n2:
            nums[k] = R[j]
            k, j = k + 1, j + 1

    def mergeSort(self, nums: List[int], l: int, r: int) -> None:
        if l < r:
            m = (l + r) // 2
            self.mergeSort(nums, l, m)
            self.mergeSort(nums, m + 1, r)
            self.merge(nums, l, m, r)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums