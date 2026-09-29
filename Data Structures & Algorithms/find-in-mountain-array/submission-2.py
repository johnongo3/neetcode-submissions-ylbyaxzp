class Solution:
    def binSearch(self, l: int, r: int, target: int, arr: 'MountainArray', ascending: bool) -> int:
        if l > r:
            return -1

        mid = l + (r - l) // 2
        if arr.get(mid) == target:
            return mid

        if ascending:
            if target < arr.get(mid):
                return self.binSearch(l, mid - 1, target, arr, True)
            else:
                return self.binSearch(mid + 1, r, target, arr, True)
        else:
            if target > arr.get(mid):
                return self.binSearch(l, mid - 1, target, arr, False)
            else:
                return self.binSearch(mid + 1, r, target, arr, False)
        
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find peak with binary search
        # if midpoint is bigger than left, pull left in
        # if mid point is smaller than left, pull right in
        # return peak
        # can break up the mountainArr into 2 separate arrays.
        # [0, k] and [k + 1, len(mountainArr)] and binary search respectively

        # find the peak, left binary search
        n = mountainArr.length()
        
        # 1. Correctly find the peak index
        l_peak, r_peak = 0, n - 1
        while l_peak < r_peak:
            mid = l_peak + (r_peak - l_peak) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l_peak = mid + 1
            else:
                r_peak = mid

        idx_peak = l_peak

        # 2. Binary search the ascending left side
        first_search = self.binSearch(0, idx_peak, target, mountainArr, ascending=True)
        if first_search != -1:
            return first_search
        
        # 3. Binary search the descending right side
        second_search = self.binSearch(idx_peak + 1, n - 1, target, mountainArr, ascending=False)

        return second_search