class Solution:    
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sort(self, nums: List[int], left: int, right: int) -> List[int]:
        if left > right:
            return []

        n = right - left + 1
        if n == 1:
            return [nums[left]]
        if n == 2:
            if nums[left] < nums[right]:
                return [nums[left], nums[right]]
            return [nums[right], nums[left]]

        mid = left + (right - left) // 2
        left_sorted = self.merge_sort(nums, left, mid)
        right_sorted = self.merge_sort(nums, mid + 1, right)
        return self.merge_step(n, left_sorted, right_sorted)

    def merge_step(self, n: int, left_sorted: List[int], right_sorted: List[int]) -> List[int]:
        i = 0
        j = 0
        result = []
        while i < len(left_sorted) and j < len(right_sorted):
            left_value = left_sorted[i]
            right_value = right_sorted[j]

            if left_value < right_value:
                result.append(left_value)
                i += 1
            else:
                result.append(right_value)
                j += 1

        print(left_sorted, right_sorted)
        while i < len(left_sorted):
            result.append(left_sorted[i])
            i += 1

        while j < len(right_sorted):
            result.append(right_sorted[j])
            j += 1
        return result
        