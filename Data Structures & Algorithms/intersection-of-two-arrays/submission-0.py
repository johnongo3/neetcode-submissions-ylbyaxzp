class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        nums1 = set(nums1)
        for num in list(nums1):
            if num not in nums2:
                nums1.discard(num)
        return list(nums1)