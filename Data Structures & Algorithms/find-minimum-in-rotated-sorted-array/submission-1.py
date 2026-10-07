class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1       # Minimum is strictly right of m
            else:
                r = m           # Minimum could be at m, so don't exclude it (-1)
        return nums[l]