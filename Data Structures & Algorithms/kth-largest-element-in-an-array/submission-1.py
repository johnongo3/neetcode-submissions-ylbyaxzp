class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
        k_largest = heapq.nlargest(k,heap)
        return k_largest[-1]