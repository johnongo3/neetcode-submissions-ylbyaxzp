class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total_prod = nums[0]
        total_prod_no_zero = nums[0]
        res = []
        # get the total product of the array
        for i in range(1, len(nums)):
            total_prod *= nums[i]
            if nums[i] != 0:
                total_prod_no_zero *= nums[i]

        
        # for each idx, divide the total_prod by nums[idx]
        for num in nums:
            if num == 0 and nums.count(0) <= 1:
                res.append(int(total_prod_no_zero))
            elif num == 0:
                res.append(int(total_prod))
            else:
                res.append(int(total_prod / num))

        return res