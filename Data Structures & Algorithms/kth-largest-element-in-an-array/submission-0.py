class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)

        i = 0
        res = 0
        while i < k:
            res = heapq.heappop_max(nums)
            i += 1

        return res