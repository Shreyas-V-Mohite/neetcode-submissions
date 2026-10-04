class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums)) # this is required as on line 7 error thorwn : list assignment index out of range
        pre = 1
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]
        pos = 1
        for i in range(len(nums)-1, -1 , -1):
        # starts the loop at the last array index, steps backward by one, and stops before -1 to include index zero.
            output[i] *= pos
            pos *= nums[i]
        return output